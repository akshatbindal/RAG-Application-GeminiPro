from pypdf import PdfReader
import re

def load_pdf(file_path):
    # Logic to read pdf
    reader = PdfReader(file_path)

    # Loop over each page and store it in a variable
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text

def split_text(text: str):
    split_text = re.split('\n \n', text)
    return [i for i in split_text if i != ""]
