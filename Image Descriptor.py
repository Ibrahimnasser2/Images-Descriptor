## Image Descriptor

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai





# configuring API key
genai.configure(api_key="AIzaSyCSqoXVBrYyrCSt3q5E0f09T7ydnBwrHRE")

## function to load Gemini Pro vision model and get response
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(Image):
    #loading the gemini model
    input=" you have an image.tell me what are in  it ?with details  "
    
    response = model.generate_content([input,Image])
   
    return response.text

st.set_page_config(page_title="Image Descriptor ")
st.header("Image Descriptor")


images =[]

with st.sidebar:
    st.text("welcome! plesae chosse the images ")
    
    files=st.file_uploader("chosse images",accept_multiple_files=True,type=["jpg", "jpeg", "png"])
   
if files is not None:
    for i in range(len(files)):
   
        st.image(files[i]);
    
        images.append(Image.open(files[i]))
    submit = st.button("Tell me about the images.")
    


if submit:
    if len(images)==1:
        st.subheader("The  image description is:")
        response = get_gemini_response(images[i])
        st.write(response)
    else:
        for i in range(len(images)):
                st.subheader("The {} image description is:".format(i+1))
                response = get_gemini_response(images[i])
                st.write(response)
        
        