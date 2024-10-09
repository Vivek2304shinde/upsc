from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF using PyPDF2"""
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
