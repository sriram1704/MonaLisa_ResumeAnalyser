import PyPDF2

def pdf_to_text(pdf_file):
    """
    Extract text from a PDF file.
    """
    try:
        # Check if the file is a path or a file-like object (Flask uses file-like objects)
        if isinstance(pdf_file, str):
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
        else:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        if not text.strip():
            print("No extractable text found in the PDF.")
            return None

        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
