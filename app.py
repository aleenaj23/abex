import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fpdf import FPDF

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini AI
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Latest Gemini model
        response = model.generate_content(prompt, stream=False)  # Ensure synchronous call
        return response.text if response else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Multi-Agent Workflow

# 1️⃣ Content Planning Agent: Generates a structured outline
def generate_outline(topic, keywords):
    prompt = (f"Create a structured blog outline for '{topic}' using keywords: {keywords}. "
              f"Ensure logical flow with headings and subheadings.")
    return get_gemini_response(prompt)

# 2️⃣ Content Generation Agent: Writes the blog based on the outline
def generate_blog_content(outline, tone, word_count):
    prompt = (f"Write a {tone} blog post of approximately {word_count} words based on the following outline: {outline}. "
              f"Ensure clarity and proper flow.")
    return get_gemini_response(prompt)

# 3️⃣ SEO Optimization Agent: Ensures content follows SEO best practices
def optimize_for_seo(content, keywords):
    prompt = (f"Enhance the following blog content by ensuring proper keyword placement and SEO optimization. "
              f"Ensure readability, structured headings, and SEO-friendly formatting. Keywords: {keywords}. "
              f"Content:\n{content}")
    return get_gemini_response(prompt)

# 4️⃣ Review Agent: Proofreads and improves content quality
def review_content(content):
    prompt = (f"Proofread and refine the following blog content to ensure grammar correctness, coherence, and readability. "
              f"Make it engaging and natural:\n{content}")
    return get_gemini_response(prompt)

# Streamlit App Configuration
st.set_page_config(page_title="SEO Blog Generator", layout="wide")
st.title("📝 Multi-Agent SEO Blog Generator")

# Input fields
st.subheader("Generate SEO-Optimized Blog Content")
topic = st.text_input("Enter Blog Topic:")
keyword = st.text_input("Enter Target SEO Keywords (comma-separated):")
tone = st.selectbox("Select Writing Tone:", ["Formal", "Casual", "Persuasive", "Technical"])
word_count = st.slider("Select Word Count:", min_value=300, max_value=2000, step=100, value=800)

# Initialize blog content
blog_content = ""

# Generate blog button
if st.button("🚀 Generate Blog"):
    if topic and keyword:
        st.info("🔄 Generating blog, please wait...")

        # Step 1: Generate Outline
        outline = generate_outline(topic, keyword)
        st.subheader("📌 Generated Outline:")
        st.write(outline)

        # Step 2: Generate Content Based on Outline
        blog_content = generate_blog_content(outline, tone, word_count)

        # Step 3: Optimize for SEO
        blog_content = optimize_for_seo(blog_content, keyword)

        # Step 4: Review and Refine Content
        blog_content = review_content(blog_content)

        # Display final blog content
        st.subheader("📝 Final Blog Post:")
        st.write(blog_content)
    else:
        st.error("⚠️ Please enter a blog topic and keywords.")

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
    st.subheader("📥 Download Blog Post")
    st.download_button("📄 Download as Markdown", open(md_filename, "r"), file_name=md_filename)
    st.download_button("🌐 Download as HTML", open(html_filename, "r"), file_name=html_filename)
    st.download_button("📜 Download as TXT", open(txt_filename, "r"), file_name=txt_filename)
    st.download_button("📂 Download as PDF", open(pdf_filename, "rb"), file_name=pdf_filename)
