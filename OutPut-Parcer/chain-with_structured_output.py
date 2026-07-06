from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# 1. Define Output Structure
class Facts(BaseModel):
    facts: list[str] = Field(description="List of 5 interesting facts")
    summary: str
    source: str

# 2. Model
model = ChatOllama(model="llama3.2", temperature=0.7)

# 3. Structured Model
structured_llm = model.with_structured_output(Facts)

# 4. Create Chain (Chaining works perfectly)
chain = (
    ChatPromptTemplate.from_template(
        "Give me 5 interesting facts about {topic}. Also give a short summary."
    )
    | structured_llm
)

# 5. Run the chain
result = chain.invoke({"topic": "Black Holes"})

print(result)
print("\nFacts:", result.facts)
print("Summary:", result.summary)