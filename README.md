# dogsVsCats

A simple deep learning app that predicts whether an uploaded image is of a dog or a cat using a pre-trained CNN model.

---

## Features

- Upload images (jpg, jpeg, png)
- Predict if the image is a dog or a cat
- Simple and user-friendly interface built with Streamlit

---

## Project Structure

- `app.py` — Streamlit application
- `model.h5` — Pre-trained CNN model
- `requirements.txt` — Python dependencies

---

## Deployment Issues on Streamlit Cloud

**Currently, there are known compatibility issues deploying this project on Streamlit Cloud due to the following:**

- Streamlit Cloud uses the latest Python versions (3.11+ or 3.12).
- Official TensorFlow wheels are not yet available for Python 3.11+ or 3.12.
- This results in pip errors like:

ERROR: Could not find a version that satisfies the requirement tensorflow==2.x.x

## How to Run Locally

1. Clone the repo:
 git clone 
 cd dogsVsCats
2. Install dependencies:
pip install -r requirements.txt
3. Run the app:
streamlit run app.py
