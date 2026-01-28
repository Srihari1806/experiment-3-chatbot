# 🤖 Local AI Chatbot Lab (Privacy-Focused)

> **Viva/Lab Project**: A full-stack AI application running 100% locally on Windows using Ollama (Gemma 2B) and Python Flask.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![Ollama](https://img.shields.io/badge/AI-Ollama%20(Local)-orange)
![LlamaIndex](https://img.shields.io/badge/RAG-LlamaIndex-purple)

## 🌟 Features
*   **📄 Chat with Documents**: Upload PDF, Word, or Excel files and ask questions. (Computed locally via RAG).
*   **🌐 Web Researcher**: Enter a URL and get an AI summary of the content.
*   **🔒 100% Privacy**: No data leaves your laptop. Everything runs on localhost.
*   **🎨 Premium UI**: Glassmorphism design with dark mode.

## 🚀 How to Run (Windows)
1.  **Install Ollama**: [Download Here](https://ollama.com).
2.  **Pull the Model**:
    ```bash
    ollama run gemma:2b
    ```
3.  **Run the Project**:
    Double-click `run_lab.bat`
    
    *OR manually:*
    ```bash
    pip install -r requirements.txt
    python app.py
    ```
4.  Open `http://127.0.0.1:5000`

## 🛠️ Tech Stack
*   **Backend**: Python, Flask
*   **AI Engine**: Ollama (Gemma:2b model)
*   **Orchestration**: LlamaIndex, LangChain
*   **Frontend**: HTML5, CSS3 (Vanilla)

## 📸 Screenshots
*(Add your screenshots here)*

---
*Created by [Your Name] for AD Lab Experiment 3*
