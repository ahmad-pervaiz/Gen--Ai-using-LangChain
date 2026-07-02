from langchain_ollama import ChatOllama

model=ChatOllama(
    model="llama3.2",
    temperature=0.7
)
Res=model.invoke("Tell me the meaning of the Ahmad")
print(Res)