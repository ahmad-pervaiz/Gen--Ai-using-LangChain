from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# 1. Initialize local pipeline (Downloads ~2.2 GB)
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.7,
        max_new_tokens=100
    )
)

# 2. Wrap it
model = ChatHuggingFace(llm=llm)

# 3. Invoke locally
result = model.invoke("Who is Quaid-e-Azam?")
print(result.content)