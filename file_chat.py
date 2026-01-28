import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Initialize Global Settings
# Use BAAI/bge-small-en-v1.5 as it's small, fast, and better than default OpenAI for local use
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm = Ollama(model="gemma:2b", request_timeout=300.0) 

# Global variable to store the index in memory
query_engine = None

def process_file(filepath):
    global query_engine
    
    if not os.path.exists(filepath):
        return "Error: File not found."

    try:
        # Load data
        documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
        
        # Create Vector Store Index
        index = VectorStoreIndex.from_documents(documents)
        
        # Create Query Engine
        query_engine = index.as_query_engine()
        
        return f"Successfully processed {os.path.basename(filepath)}. You can now ask questions!"
        
    except Exception as e:
        return f"Error processing file: {str(e)}"

def ask_file(query):
    global query_engine
    if query_engine is None:
        return "Please upload and process a file first."
    
    try:
        response = query_engine.query(query)
        return str(response)
    except Exception as e:
        return f"Error generating answer: {str(e)}"
