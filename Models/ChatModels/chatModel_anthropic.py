import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

# Use ChatOpenAI even for Anthropic models on GitHub Marketplace
llm = ChatOpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=github_token,
    model="meta-llama-3.1-405b-instruct"  # GitHub routes this OpenAI-styled request to Claude
)

result = llm.invoke("Who is the Quaid-e-Azam?")
print(result.content)

