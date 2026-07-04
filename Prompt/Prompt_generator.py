from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumpd
import json

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

# Save the prompt
with open("template.json", "w", encoding="utf-8") as f:
    json.dump(dumpd(prompt_template), f, indent=2)

print("✅ Prompt successfully saved as 'template.json'")