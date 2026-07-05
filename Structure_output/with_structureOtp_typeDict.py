from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

model = ChatOllama(
    temperature=0.7,
    model="llama3.2"
)

# Define structure using TypedDict
class Review(TypedDict):
    summary: Annotated[str,'A breif summary of the review']   # guiding out model exactly what to do 
    sentiment: Annotated [str, "Return sentiment of the review either negative, positive or neutral"]


# Create structured model
structured_model = model.with_structured_output(Review)

# Corrected invoke
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too
many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other
brands. Hoping for a software update to fix this.""")

print(result)
print("\nSummary:", result["summary"])
print("Sentiment:", result["sentiment"])