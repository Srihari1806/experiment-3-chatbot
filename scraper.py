import requests
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama
import re

def scrape_and_ask(url_or_topic, user_prompt=None):
    """
    Scrapes a URL or searches for a topic (simplified to just treating input as URL for now, 
    but could be expanded).
    """
    if not url_or_topic.startswith('http'):
        # If it's a topic, ideally we'd search, but for this lab, let's assume URL
        # Or we could just ask the LLM directly about the topic without scraping.
        llm = Ollama(model="gemma:2b")
        return llm.invoke(f"Tell me about: {url_or_topic}")

    url = url_or_topic
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "aside"]):
            script.extract()
            
        text = soup.get_text()
        
        # Clean text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # Limit content to ~6000 chars to fit in context window of smaller local models
        content = text[:6000]
        
        if len(content) < 100:
            return "Could not extract enough text from this website. It might be blocking scrapers."

        llm = Ollama(model="gemma:2b")
        
        if not user_prompt:
            prompt = f"Analyze the following website content and provide a comprehensive summary with key points:\n\n{content}"
        else:
            prompt = f"Use the website content below to answer this question: '{user_prompt}'\n\nWebsite Content:\n{content}"
            
        return llm.invoke(prompt)
        
    except Exception as e:
        return f"Error processing request: {str(e)}"
