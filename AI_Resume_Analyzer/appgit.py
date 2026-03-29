import streamlit as st
import google.generativeai as genai
import PyPDF2

# ✅ API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Extract PDF text
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# UI
st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description (Optional)")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):

        if not resume_text.strip():
            st.error("❌ Could not read PDF")
        else:
            with st.spinner("Analyzing... 🤖"):

                prompt = f"""
                Analyze this resume:

                Resume:
                {resume_text}

                Job Description:
                {job_description if job_description else "Not provided"}

                Give:
                1. Key Skills
                2. Strengths
                3. Weaknesses
                4. Suggestions
                5. ATS Score (out of 100)
                6. Job Match Percentage
                """

                response = model.generate_content(prompt)

                st.subheader("📊 Result")
                st.write(response.text)