import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
st.set_page_config
(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #ffffff, #eaf4ff, #dbeafe);
    color: #1e293b;
}
/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}
/* Title */
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    color: #1d4ed8;
    margin-bottom: 5px;
}
/* Subtitle */
.subtitle {
    text-align: center;
    color: #475569;
    font-size: 18px;
    margin-bottom: 35px;
}
/* Chat card */
.chat-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #bfdbfe;
    box-shadow: 0 10px 30px rgba(30, 64, 175, 0.15);
}
/* Text area label */
.stTextArea label {
    color: #1e3a8a !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}
/* Text area */
textarea {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 2px solid #bfdbfe !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}
/* Placeholder text */
textarea::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}
/* Text area focus */
textarea:focus {
    border: 2px solid #3b82f6 !important;
    box-shadow: 0 0 8px rgba(59, 130, 246, 0.25) !important;
}
/* Generate button */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    padding: 13px;
    font-size: 17px;
    font-weight: 700;
    color: white !important;
    background: linear-gradient(90deg, #2563eb, #4f46e5);
    transition: all 0.3s ease;
}
/* Button hover */
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.3);
}
/* Response box */
.response-box {
    background: #f8fafc;
    padding: 25px;
    margin-top: 25px;
    border-radius: 15px;
    border-left: 5px solid #2563eb;
    color: #1e293b;
    line-height: 1.7;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}
/* Response heading */
.response-box h3 {
    color: #1d4ed8;
}
/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">🤖 Gemini AI Chatbot</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">✨ Ask anything. Learn anything. Powered by Gemini.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="chat-card">', unsafe_allow_html=True)
prompt = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words...",
    height=150
)
if st.button("🚀 Generate Response"):
    if prompt.strip():
        with st.spinner("🤖 Gemini is thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )
                st.success("✅ Response generated!")
                st.markdown(
                    f"""
                    <div class="response-box">
                        <h3>🤖 Gemini's Response</h3>
                        {response.text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a prompt.")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">Powered by Google Gemini • Built with Streamlit 🚀</div>',
    unsafe_allow_html=True
)