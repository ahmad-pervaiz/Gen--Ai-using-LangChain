from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize Model
model = ChatOllama(model="llama3.2", temperature=0.7)

# Create Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words for a beginner."
)

# Create Output Parser
output_parser = StrOutputParser()

# Create Chain (Correct way)
chain = prompt | model | output_parser

# Run the chain
result = chain.invoke({"topic": "LangChain"})

print(result)