import streamlit as st
import base64
from tempfile import NamedTemporaryFile
import os
import requests

# Set the page configuration
st.set_page_config(
    page_title="Question Generator App",
    page_icon="📄",
    layout="wide"
)

# Custom CSS to enhance the look and feel
st.markdown("""
    <style>
    /* Main page styles */
    .main {
        background-color: #f5f5f5;
        font-family: "Helvetica Neue", sans-serif;
        padding: 20px;
    }
    /* Title styles */
    .title {
        font-size: 2.5em;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }
    /* Introduction styles */
    .intro {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    /* Question styles */
    .question {
        font-size: 1.1em;
        color: #333;
        margin-bottom: 10px;
    }
    /* Download button styles */
    .download-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    /* Footer styles */
    .footer {
        font-size: 0.9em;
        color: #999;
        text-align: center;
        margin-top: 30px;
    }
    /* Warning message styles */
    .warning {
        font-size: 1em;
        color: #FF6347; /* Red color */
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">📄 Question Generator App</div>', unsafe_allow_html=True)

# Introduction
st.markdown('<div class="intro">Upload a PDF file to generate questions based on its content:</div>', unsafe_allow_html=True)

# File upload and processing
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    if uploaded_file.type != 'application/pdf':
        st.error('Please upload a PDF file.')
    else:
        with st.spinner('Processing PDF...'):
            with NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            with open(tmp_file_path, 'rb') as f:
                pdf_data = f.read()

            url = 'https://phmzcyx66k.execute-api.us-east-1.amazonaws.com/pdf_ques_gen/upload_pdf'

            headers = {
                'Content-Type': 'application/pdf',
            }

            response = requests.post(url, data=pdf_data, headers=headers)

            if response.status_code == 200:
                st.success('Questions Generated Successfully!')

                questions = response.json()['generated_question']

                for i, question in enumerate(questions):
                    st.markdown(f'<div class="question">{question}</div>', unsafe_allow_html=True)

                st.markdown('<div class="download-button">', unsafe_allow_html=True)
                st.download_button(
                    label="Download Questions",
                    data="\n".join([f"{question}" for question in questions]),
                    file_name='generated_questions.txt',
                    mime='text/plain'
                )
                st.markdown('</div>', unsafe_allow_html=True)

                os.remove(tmp_file_path)

            else:
                st.error(f'Failed to upload PDF to Lambda function with status code {response.status_code}')
                st.error("Operation failed. Please try again.")

# Footer
st.markdown('<div class="footer">---<br>Note: This app is created for generating questions from uploaded PDF files using advanced language processing techniques. Each question aims to facilitate deeper understanding and discussion based on the document content.</div>', unsafe_allow_html=True)
