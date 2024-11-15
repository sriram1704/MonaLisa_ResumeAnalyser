# MonaLisa Resume Assistant

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange)

MonaLisa Resume Assistant is a web application designed to help job seekers match their resumes with job descriptions. The application uses a pre-trained machine learning model to analyze the relevance of a resume for a specific job description and provides a match score.

## 📝 Project Overview
**MonaLisa Resume Assistant** is an AI-powered tool that helps users match their resumes with job descriptions to improve their chances of landing interviews. The application is built using Flask for the backend and a pre-trained machine learning model for resume analysis.

### ⚡ Features
- Upload your resume (PDF format) and paste a job description to get a match score.
- Uses NLP techniques to categorize resumes and calculate relevance scores.
- User-friendly web interface with responsive design.
- Built with scalable technologies, suitable for deployment on cloud platforms.

---

## 🛠️ Technologies Used
- **Languages**: Python, HTML, CSS, JavaScript
- **Frameworks**: Flask, Bootstrap
- **Libraries**: scikit-learn, PyPDF2, joblib, pdfplumber (optional for PDF extraction)
- **Tools**: Pre-trained machine learning model (`resume_matcher_model.pkl`)

---

## 🤖 Machine Learning Model
The core of this project is a machine learning model that uses **Natural Language Processing (NLP)** to analyze resumes.

### How It Works:
1. **Text Extraction**: Extracts text from PDF resumes using `PyPDF2`.
2. **Text Vectorization**: Uses `TfidfVectorizer` from `scikit-learn` to convert text into numerical vectors.
3. **Cosine Similarity**: Calculates the similarity score between the resume and job description.
4. **Classification**: The model categorizes the resume into domains (e.g., Data Science, Software Engineering).

---

## 🛠️ Installation and How to Run the Project

### Prerequisites
- **Python 3.7+** must be installed on your system.
- **pip** (Python package installer) should be set up.
- **Git** (for cloning the repository).

### Step 1: Clone the Repository
First, clone this repository to your local machine using Git:
```bash
git clone https://github.com/yourusername/mona-lisa-resume-assistant.git
cd mona-lisa-resume-assistant
