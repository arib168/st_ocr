#magic command to create a python file from ipynb
#takes the entire code and puts it in app.py since streamlit runs only on COMMAND LINE INTERFACE(CLI)  using  .py files
import numpy as np
import streamlit as st 
import cv2
import pytesseract
from PIL import Image   #python imaging library, to open image, streamlit doesn't support cv2 directly to display
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.set_option('deprecation.showfileUploaderEncoding', False)  #to warning ignore 
st.title("OCR - Optical Character Recognition")  #print title and text
st.text("Upload the Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...",  type=["jpg","png","jpeg"]) #we can upload these types of files
if uploaded_file is not None: #only if file is uploaded it will show, else no error and nothing happens

        img = Image.open(uploaded_file)  #reads the image, similar to imread
        
        st.image(img, caption='Uploaded Image',use_column_width=True)  #displays image, caption is uploaded image, uses image width 

        st.write("")   #print blank space

        if st.button('PREDICT'):    #creates one button called predict
                st.write("Result...")   #prints result 
                extractedInformation = pytesseract.image_to_string(img)   #pytesseract converts img to text and prints
                st.title(extractedInformation)
