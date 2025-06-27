import streamlit as st
import cv2
import numpy as np

# Title
st.title("Face Detection App using Haar Cascade")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image as bytes -> numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Convert image BGR to RGB for display in Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Show image with detections
    st.image(img_rgb, caption='Detected Faces', use_column_width=True)

    st.write(f"Found {len(faces)} face(s).")
