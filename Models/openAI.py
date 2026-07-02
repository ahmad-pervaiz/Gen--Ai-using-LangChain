from langchain_openai import ChatOpenAI

# Initialize the model using GitHub's free endpoint
model = ChatOpenAI(
    openai_api_key="",
    openai_api_base="",
    model="gpt-4o-mini" # or "meta-llama-3-70b-instruct"
)

response = model.invoke("Explain LangChain in one sentence.")
print(response.content)