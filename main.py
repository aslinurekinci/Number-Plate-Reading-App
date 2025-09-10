#library
import cv2
from PIL import Image
import streamlit as st
from helper import detect_plate


#title
st.title("Plate Recognition System🚗")

#header
st.header("Upload an Image")

#files
file=st.file_uploader("",type=["png","jpg","jpeg"])

#model
model_path="models/plate_detection.pt"


#ımages
if file is not None:
    #original image
    st.header("Original Image")
    image=Image.open(file).convert('RGB')
    st.image(image, use_container_width=True)

    #processed image
    st.header("Detection Result")
    detection_result,cropped_image,is_detected=detect_plate(image,model_path)

    if is_detected is not 0:
       st.write("#### [INFO].. Plate is detected: ",is_detected)
       st.image(detection_result, use_container_width=True)
       st.image(cropped_image, use_container_width=True)

    else:
        st.write("#### [INFO].. Plate is not detected: ",is_detected)
        st.image(detection_result, use_container_width=True)
     

 
