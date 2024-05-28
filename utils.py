import streamlit as st
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 300px;
        width: 300px;
        height: 300px;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
