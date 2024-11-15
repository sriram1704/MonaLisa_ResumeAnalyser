from flask import Flask, render_template, request, jsonify
import os
from utils import pdf_to_text
from resume_matcher_model import ResumeMatcherModel
from data_processor import DataProcessor

app = Flask(__name__)

# Load the pre-trained model and vectorizer
model_path = "resume_matcher_model.pkl"
vectorizer_path = "vectorizer.pkl"
resume_matcher_model = ResumeMatcherModel(vectorizer=None)
resume_matcher_model.load_model(model_path, vectorizer_path)

def extract_text_from_pdf(pdf_file):
    """Extract text from the uploaded PDF file."""
    return pdf_to_text(pdf_file)

def read_text_file(file):
    """Read the contents of a text file."""
    return file.read().decode('utf-8').strip()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match_resume():
    """Handle the prediction of category and match score."""
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume uploaded'}), 400
    
    resume_file = request.files['resume']
    job_description = request.form.get('job_description', '')

    if not job_description:
        return jsonify({'error': 'Job description is required'}), 400

    # Extract text from the uploaded PDF resume
    print("Extracting text from the PDF...")
    resume_text = pdf_to_text(resume_file)
    
    if not resume_text:
        return jsonify({'error': 'Could not extract text from the resume'}), 500

    # Predict category and match percentage
    category = resume_matcher_model.predict_category(resume_text)
    match_percentage = resume_matcher_model.calculate_match_percentage(resume_text, job_description)

    return jsonify({
        'category': category[0],
        'score': round(match_percentage, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
