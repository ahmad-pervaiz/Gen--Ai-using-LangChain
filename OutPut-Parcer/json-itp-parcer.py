from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Initialize Model
model = ChatOllama(model="llama3.2", temperature=0)

# Create Prompt
prompt = ChatPromptTemplate.from_template(
    """Return the following information in JSON format:
    
    Topic: {topic}
    
    Provide the answer as valid JSON with these keys:
    - name
    - description
    - difficulty_level
    - key_features (list)
    """
)

# Create JSON Output Parser
json_parser = JsonOutputParser()

# Create Chain
chain = prompt | model | json_parser

# Run
result = chain.invoke({"topic": "LangChain"})

print(result)
print("\nType:", type(result))
