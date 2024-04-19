import streamlit as st

from PIL import Image

# Set page title and layout
st.set_page_config(page_title="Navigator", layout="wide")

# Display the page title
st.title("Unpacking Your Business Using Vectara")


# Load the image from the data folder
image_path = 'data/title.png'
image = Image.open(image_path)

# Display the image in the Streamlit app
st.image(image, caption='Image from title.png')

