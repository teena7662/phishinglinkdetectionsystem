import streamlit as st
import pickle
import pandas as pd
from feature_extractor import extract_features

# Load model
model = pickle.load(open('phishing_model.pkl', 'rb'))

st.title("🔐 Phishing Website Detector")

url = st.text_input("Enter a website URL")

if st.button("Check"):
    if url:
        # Extract features
        features = extract_features(url)
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)[0]

        if prediction == 1:
            st.error("⚠️ This website is likely a **Phishing** site.")
        else:
            st.success("✅ This website is **Legitimate**.")
    else:
        st.warning("Please enter a URL.")
