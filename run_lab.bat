@echo off
title AI Chatbot Lab - Runner

echo ==================================================
echo       AI Chatbot Lab - Starting Up...
echo ==================================================
echo.

echo [1/5] Checking Ollama...
where ollama >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Ollama is not installed or not in PATH.
    echo Please install standard Ollama for Windows from https://ollama.com
) else (
    echo [OK] Ollama found. Ensure 'ollama serve' is running in background.
)

echo [2/5] Switching to Low-Memory Model (Gemma 2B)...
echo This fits your available RAM (2.5GB available / 4.6GB needed for Llama3).
call ollama pull gemma:2b

echo [3/5] Activating Virtual Environment...
if not exist venv\Scripts\activate.bat goto :NoVenv

call venv\Scripts\activate.bat

echo [4/5] Verifying Dependencies...
pip install -r requirements.txt

goto :Launch

:NoVenv
echo [ERROR] Virtual environment not found (venv)!
echo Creating new virtual environment...
python -m venv venv
call venv\Scripts\activate.bat
echo Installing dependencies...
pip install -r requirements.txt

:Launch
echo [5/5] Launching Web Application...
echo.
echo NOTE: First run might take time to download the embedding model.
echo Open your browser to: http://127.0.0.1:5000
echo.
python app.py

pause
