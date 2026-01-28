# 🎓 Viva & Lab Guide - AI Chatbot Project
> **Project Name:** Local AI Chatbot Lab (RAG + Web Scraping)  
> **Tech Stack:** Python, Flask, Ollama, LangChain/LlamaIndex, Windows.

---

## 🗣️ How to Introduce Your Project
**Examiner:** "What have you built?"  
**You:**  
"I have built a **Privacy-Focused AI Chatbot** that allows users to chat with their documents (PDFs, Excel, Word) and scrape websites for summaries. 
Unlike typical chatbots, this system runs **100% locally** on this machine using Ollama and Llama3, meaning no data is sent to the cloud. It combines **RAG (Retrieval Augmented Generation)** for documents and **Real-time Scraping** for web content."

---

## 🏗️ Architecture (Mental Model)
Visualize the flow:

1. **User Input** (File or URL) -> **Frontend** (HTML/JS)
2. **BackendAPI** (Flask) receives request.
3. **If Document:**
   - Text Extracted -> **Embeddings** (Vector representation) -> **Vector Store** (Index).
   - Question -> Search Vector Store -> **Context** -> **Ollama LLM** -> Answer.
4. **If Website:**
   - **BeautifulSoup** fetches HTML -> Clean Text -> **Ollama LLM** -> Summary.

---

## ❓ Common Viva Questions & Answers

### Q1: Why did you use Ollama?
**A:** Ollama allows us to run powerful LLMs like Llama3 locally. It allows for free, offline inference without needing API keys from OpenAI/Google, making it perfect for secure enterprise or lab environments.

### Q2: What is LangChain/LlamaIndex used for?
**A:** These are orchestration frameworks.
- **LlamaIndex** is used here for the **RAG pipeline**: it handles chunking documents, creating embeddings, and retrieving relevant context for the LLM.
- **LangChain** (or direct integration) is used to interface with the LLM for general prompts.

### Q3: How does the "Chat with Document" work?
**A:** It uses **RAG (Retrieval Augmented Generation)**.
1. The document is broken into small chunks of text.
2. An **Embedding Model** converts these chunks into number vectors.
3. When you ask a question, your question is also converted to a vector.
4. We find the most similar chunks (mathematically close vectors) and send them to the LLM to generate the answer.

### Q4: Why Flask instead of Django?
**A:** Flask is micro-framework and lightweight. For a specific tool like this where we primarily need API endpoints for a Single Page Application (SPA), Flask is more efficient and easier to set up than Django.

### Q5: Can this handle large files?
**A:** Yes, LlamaIndex handles large files by "chunking" them. However, processing time depends on the local CPU/GPU speed.

---

## 🛠️ Deployment Steps Recap
1. `ollama run llama3` (Starts the LLM server)
2. `python app.py` (Starts the Web Backend)
3. Open `localhost:5000`

---

## 🧪 Future Improvements (If asked)
- Add a persistent Vector Database (like ChromaDB or Weaviate) to save chats between sessions.
- Add user authentication.
- Support multiple files at once.
