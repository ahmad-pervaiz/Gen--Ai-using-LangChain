from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

# 1. Define structure using Pydantic
class Facts(BaseModel):
    facts: list[str] = Field(description="List of 5 interesting facts")

# 2. Model
model = ChatOllama(model="llama3.2", temperature=0.7)

# 3. Structured Output
structured_llm = model.with_structured_output(Facts)

# 4. Run
result = structured_llm.invoke("Give me 5 interesting facts about black holes")

print(result)
print(result.facts)        # Easy access

 

structured_llm = model.with_structured_output(
    Facts, 
    method="json_mode"      # This returns dict instead of Pydantic object
)

result = structured_llm.invoke("Give me 5 facts about black holes")
print(result)