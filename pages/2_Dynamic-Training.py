import streamlit as st
import os

# Title for your Streamlit app
st.title('SMA - Dynamic Training')

# Path to the video file within the data folder
video_file_path = 'data/sma.mp4'

# Check if the video file exists in the specified path
if os.path.exists(video_file_path):
    # Open the video file
    video_file = open(video_file_path, 'rb')
    video_bytes = video_file.read()
    # Display the video player with the video
    st.video(video_bytes)
else:
    # Display an error message if the video file is not found
    st.error('Video file not found!')

