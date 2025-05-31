import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

st.title("Dog vs Cat Predictor")
st.write("Upload an image of a dog or a cat and let the model predict!")

model = load_model("model.h5")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:

    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_container_width=True)

    # Resize to the same size used during training
    img = img.resize((64, 64))  # Match training dimensions
    img_array = image.img_to_array(img)  # Convert to array (shape: (64, 64, 3))
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 64, 64, 3)
    img_array = img_array / 255.0  # Normalize

    prediction = model.predict(img_array)[0][0]
    result = "Dog" if prediction > 0.5 else "Cat"
    st.write(f"### Prediction: {result}")
