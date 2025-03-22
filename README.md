# **Multi-Agent SEO Blog Generator**  

A **Streamlit-based AI-powered web application** that uses **Google Gemini AI** to generate **SEO-optimized blog content** based on user input. This tool streamlines blog creation for **content creators, marketers, and bloggers**, ensuring high-quality, structured, and keyword-rich blog posts.  

## **📌 System Architecture**  
The **Multi-Agent SEO Blog Generator** follows a **modular architecture** with clearly defined components:

| **Component**             | **Description**  |
|---------------------------|-----------------|
| **User Interface (Streamlit Web App)** | Provides an interactive UI for users to input blog topics, keywords, tone, and word count. Displays generated content and download options. |
| **Multi-Agent System** | Includes multiple agents: Research Agent, Content Planning Agent, Content Generation Agent, SEO Optimization Agent, and Review Agent. |
| **Backend Processing** | Uses Google Gemini AI for text generation, integrates with FPDF for PDF downloads, and dynamically stores user input. |

---

## **⚙️ Agent Workflow**  

| **Step** | **Description** |
|---------|---------------|
| **1️⃣ User Input** | User enters blog topic, SEO keywords, preferred tone, and word count. |
| **2️⃣ Research Agent** | Gathers topic-related insights for relevance. |
| **3️⃣ Content Planning Agent** | Creates a structured blog outline based on SEO principles. |
| **4️⃣ Content Generation Agent** | Uses **Google Gemini AI** to generate blog content. |
| **5️⃣ SEO Optimization Agent** | Enhances content with proper keyword placement. |
| **6️⃣ Review Agent** | Ensures coherence, grammar, and readability. |
| **7️⃣ Output & Download** | Displays the final blog and provides multiple download options. |

---

## **🛠️ Tools & Frameworks Used**  

| **Component** | **Technology Used** |
|--------------|---------------------|
| **Frontend** | Streamlit (Python) |
| **AI Model** | Google Gemini AI |
| **SEO Optimization** | NLP Techniques |
| **File Formats** | Markdown, HTML, TXT, PDF |
| **Backend Processing** | Python |
| **PDF Generation** | FPDF |

---

## **🚀 Installation & Execution Steps**  

| **Step** | **Command / Action** |
|---------|----------------------|
| **1️⃣ Clone the Repository** | ```git clone https://github.com/your-username/seo-blog-generator.git && cd seo-blog-generator``` |
| **2️⃣ Create a Virtual Environment (Optional but Recommended)** | ```python -m venv venv && source venv/bin/activate``` *(For Windows: `venv\Scripts\activate`)* |
| **3️⃣ Install Dependencies** | ```pip install -r requirements.txt``` |
| **4️⃣ Set Up API Key** | Create a `.env` file in the project root and add your API key: <br> ```GOOGLE_API_KEY=your_api_key_here``` |
| **5️⃣ Run the Application** | ```streamlit run app.py``` |
| **6️⃣ Use the Application** | Enter blog details, generate content, and download in various formats. |

---

