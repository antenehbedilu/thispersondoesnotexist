import streamlit as st
from requests import get

#set the title of the web application
st.title('This Person Does Not Exist')
#display a caption beneath the title
st.caption('a website that uses artificial intelligence (AI) to generate realistic human faces that do not actually exist.')

#retrieve the image from the FastAPI app
image = get('http://10.10.10.231:8088/api/person').content
#display the retrieved image with a caption and width of 300 pixels
st.image(image, caption='image by thispersondoesnotexist.com', width = 300)
#create a button to refresh the API call
st.button('Refresh')
