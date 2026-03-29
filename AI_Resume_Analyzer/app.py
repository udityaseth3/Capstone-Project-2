import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

#StreamlitUI
st.title("📄 AI Resume Analyzer ")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):
        prompt = f"""
        Analyze the following resume:

        {resume_text}

        Give:
        1. Key Skills
        2. Strengths
        3. Weaknesses
        4. Suggestions for Improvement
        5. Resume Score 
        """

        response = model.generate_content(prompt)
        st.write(response.text)
