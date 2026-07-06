from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Step 1: Define the structure using Pydantic
class Review(BaseModel):
    summary: str = Field(description="Short summary of the review")
    sentiment: str = Field(description="positive, negative, or neutral")
    pros: list[str] = Field(description="List of positive points")
    cons: list[str] = Field(description="List of negative points")

# Step 2: Create Parser
parser = PydanticOutputParser(pydantic_object=Review)

# Step 3: Create Prompt with format instructions
prompt = PromptTemplate(
    template="""Analyze this review and return structured data.

Review: {review_text}

{format_instructions}""",
    input_variables=["review_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Step 4: Create Chain
model = ChatOllama(model="llama3.2", temperature=0)

chain = prompt | model | parser

# Step 5: Run
review = "The phone is great but too expensive and heavy."
result = chain.invoke({"review_text": review})

print(result)
print("Summary:", result.summary)
print("Sentiment:", result.sentiment)