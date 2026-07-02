from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

# Pull the token out of the environment variables
github_token = os.getenv("GITHUB_TOKEN")

# Initialize ChatOpenAI pointing to the GitHub Marketplace Models endpoint
llm = ChatOpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=github_token,
    model="gpt-4o-mini",
    max_completion_tokens=20
)

# Invoke the model with the correct spelling
result = llm.invoke("Who is the Quaid-e-Azam?")

# Print just the clean text response
print(result.content)