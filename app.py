import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import file_chat
import scraper

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat_document', methods=['POST'])
def chat_document():
    query = request.form.get('query')
    file = request.files.get('file')
    
    if file and file.filename != '':
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process the file (Indexing)
            status = file_chat.process_file(filepath)
            if "Error" in status:
                return jsonify({'response': status})
        else:
            return jsonify({'response': "Invalid file type. Please upload PDF, Word, or Excel."})
    
    if not query:
        return jsonify({'response': "File processed. What would you like to ask?"})
        
    # Get answer
    response = file_chat.ask_file(query)
    return jsonify({'response': response})

@app.route('/scrape_web', methods=['POST'])
def scrape_web():
    data = request.json
    url = data.get('url')
    prompt = data.get('prompt')
    
    if not url:
        return jsonify({'response': "Please provide a URL."})
        
    response = scraper.scrape_and_ask(url, prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    print("Starting AI Chatbot Lab on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
