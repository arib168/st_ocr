import streamlit as st 
import cv2
import pytesseract
from PIL import Image  #Python Imaging library #to open images 
import numpy as np 

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.title("Optical Character Recognition (OCR) :")
st.text("Upload the Image :")

uploaded_file = st.sidebar.file_uploader("Choose an image :", type =["jpg","png","jpeg"]) 
if uploaded_file is not None: #if there is some file uploaded here, then do the following 
  img = Image.open(uploaded_file) #reads the file uploaded (similar to cv2.imread)
  st.write("") 
  if st.button("PREDICT"):
    st.write("Result :")
    info = pytesseract.image_to_string(img) #ocr is applied using pytesseract
    st.title(info)
