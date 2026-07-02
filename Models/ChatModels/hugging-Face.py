import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()
hugg_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# 1. Initialize the Hugging Face Endpoint (Fixed repo_id and added token)
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hugg_token
)

# 2. Wrap it in ChatHuggingFace to use standard chat messages
model = ChatHuggingFace(llm=llm)

# 3. Invoke the model with corrected spelling
result = model.invoke("Who is Quaid-e-Azam?")

# 4. Print the text content
print(result.content)