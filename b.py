import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import numpy as np
import tempfile  # For handling temporary file creation

# Install Tesseract if it's not installed
import os
if not os.path.isfile('/usr/bin/tesseract'):
    os.system('sudo apt-get install tesseract-ocr')
    
poppler_path = r'E:\New folder\poppler-24.09.0' 

# Convert PDF to images
def pdf_to_images(pdf_file):
    images = convert_from_path(pdf_file)
    return images

# Streamlit App
def main():
    st.title("Document to Text Converter Using OCR")
    
    # Upload document (PDF or image)
    uploaded_file = st.file_uploader("Upload a Document (PDF)", type=["png", "jpg", "jpeg", "pdf"])

    if uploaded_file is not None:
        file_type = uploaded_file.type

        if file_type == "application/pdf":
            st.write("Processing PDF...")

            # Save the uploaded PDF to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(uploaded_file.getbuffer())  # Write uploaded PDF to temp file
                temp_pdf_path = temp_pdf.name  # Get the file path

            # Convert PDF to images
            pdf_images = pdf_to_images(temp_pdf_path)



if __name__ == "__main__":
    main()
