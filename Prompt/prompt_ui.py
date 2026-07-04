import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.set_page_config(page_title="Research Paper Explainer", layout="centered")
st.title("📚 Research Paper Explainer Tool")

# Model
model = ChatOllama(
    temperature=0.7,
    model="llama3.2"
)

# User Inputs
paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

# Define Prompt Directly (No JSON needed)
prompt_template = PromptTemplate.from_template("""
You are a world-class AI researcher and educator.

Paper Title: {paper_input}
Desired Style: {style_input}
Desired Length: {length_input}

Explain this research paper in a {style} manner.
Provide a {length} explanation.

Structure your response with:
- Key Problem & Motivation
- Main Innovation / Contribution
- Methodology Overview
- Results & Impact
- Why This Paper Matters

Be accurate, clear, and engaging.
""")

if st.button("Generate Explanation", type="primary"):
    with st.spinner("Generating explanation..."):
        chain = prompt_template | model
        
        response = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
            "style": style_input.lower(),
            "length": length_input.lower()
        })
        
        st.success("✅ Done!")
        st.markdown("### Explanation:")
        st.write(response.content)