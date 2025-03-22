import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fpdf import FPDF

# Load environment variables
load_dotenv()

# Configure Gemini API with the correct model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini AI
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct model
        response = model.generate_content(prompt, stream=False)  # Ensure synchronous call
        return response.text if response else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App Configuration
st.set_page_config(page_title="SEO Blog Generator", layout="wide")
st.title("Multi-Agent SEO Blog Generator")

# Input fields
st.subheader("Generate SEO-Optimized Blog Content")
topic = st.text_input("Enter Blog Topic:")
keyword = st.text_input("Enter Target SEO Keywords (comma-separated):")
tone = st.selectbox("Select Writing Tone:", ["Formal", "Casual", "Persuasive", "Technical"])
word_count = st.slider("Select Word Count:", min_value=300, max_value=2000, step=100, value=800)

# Initialize blog content
blog_content = ""

# Generate blog button
if st.button("Generate Blog"):
    if topic and keyword:
        st.info("Generating blog, please wait...")
        prompt = (f"Generate an SEO-optimized blog post on '{topic}'. Include keywords: {keyword}. "
                  f"Maintain a {tone} tone. Keep it within {word_count} words.")
        blog_content = get_gemini_response(prompt)
        st.subheader("Generated Blog Post:")
        st.write(blog_content)
    else:
        st.error("Please enter a blog topic and keywords.")

# Function to save blog in different formats
def save_file(content, filename, mode="w"):
    with open(filename, mode) as f:
        f.write(content)

# Provide download options if content is generated
if blog_content:
    # Save in Markdown
    md_filename = "blog.md"
    save_file(blog_content, md_filename)

    # Save in HTML
    html_filename = "blog.html"
    save_file(f"<html><body><p>{blog_content}</p></body></html>", html_filename)

    # Save in TXT
    txt_filename = "blog.txt"
    save_file(blog_content, txt_filename)

    # Save in PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, blog_content)
    pdf_filename = "blog.pdf"
    pdf.output(pdf_filename)

    # Streamlit download buttons
    st.subheader("Download Blog Post")
    st.download_button("Download as Markdown", open(md_filename, "r"), file_name=md_filename)
    st.download_button("Download as HTML", open(html_filename, "r"), file_name=html_filename)
    st.download_button("Download as TXT", open(txt_filename, "r"), file_name=txt_filename)
    st.download_button("Download as PDF", open(pdf_filename, "rb"), file_name=pdf_filename)
