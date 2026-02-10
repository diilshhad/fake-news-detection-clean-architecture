import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from predict import predict_news

st.title("📰 Fake News Detection System")

st.write("Enter a news headline or article text")

user_input = st.text_area("Enter News Text")

if st.button("Check News"):

    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            with st.spinner("Analyzing..."):
                label, confidence = predict_news(user_input)
            
            if label == "REAL":
                st.success(f"Prediction: REAL")
            else:
                st.error(f"Prediction: FAKE")
            
            st.info(f"Confidence Score: {confidence:.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write(e)
