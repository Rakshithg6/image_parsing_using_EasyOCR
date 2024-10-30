import streamlit as st
import fitz
from PIL import Image
import easyocr
import io
import os
import numpy as np

# Initialize EasyOCR reader (only needs to be done once)
reader = easyocr.Reader(['en'])

def extract_images_from_pdf(pdf_file):
    images = []
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img = Image.open(io.BytesIO(image_bytes))
            images.append(img)
    return images

def extract_text_from_images(images):
    text_list = []
    for img in images:
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        try:
            # EasyOCR expects either a file path or numpy array
            img_array = Image.open(img_bytes)
            # Convert PIL Image to numpy array
            img_array = np.array(img_array)
            # Perform OCR using EasyOCR
            results = reader.readtext(img_array)
            # Extract text from results
            text = ' '.join([result[1] for result in results])
            text_list.append(text)
        except Exception as e:
            st.error(f"An error occurred while processing an image: {e}")
    return text_list

st.title('PDF Image Text Extraction')

uploaded_pdf = st.file_uploader("Choose a PDF file...", type=["pdf"])

if uploaded_pdf is not None:
    if st.button('Upload and Process'):
        images = extract_images_from_pdf(uploaded_pdf)
        if images:
            try:
                text_list = extract_text_from_images(images)
                st.success("Text extracted successfully.")
                for i, text in enumerate(text_list):
                    st.write(f"Image {i+1} Text:")
                    st.text(text)
            except Exception as e:
                st.error(f"Failed to process images due to: {e}")
        else:
            st.write("No images found in the PDF.")