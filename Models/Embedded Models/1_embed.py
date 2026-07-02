# code for the open-Ai APi key 
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()

# embeeding=OpenAIEmbeddings(
#     model="gpt-mini",
#     dimentions=32
# )
# res=embeeding.embed_query("Lahore is beautiful city of Pakistan")
# print(str(res))




# code  with using the student developer pach github token 
import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
github_token = os.getenv("GITHUB_TOKEN") # Using your GitHub Student pack token

# Initialize OpenAIEmbeddings pointing to the GitHub Serverless endpoint
embeddings = OpenAIEmbeddings(
    base_url="https://models.inference.ai.azure.com",
    api_key=github_token,
    model="text-embedding-3-small",  # Corrected to a valid, hosted embedding model
    dimensions=32                   # Corrected spelling of 'dimensions'
)

# Embed the query
res = embeddings.embed_query("Lahore is beautiful city of Pakistan")

# Print the resulting numerical vector array
print(res)
