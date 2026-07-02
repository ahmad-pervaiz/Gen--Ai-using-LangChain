from langchain_ollama import OllamaEmbeddings

# Initialize local embedding model
embedding = OllamaEmbeddings(model="llama3.2")

doc = [
    "hello im ahmad",
    "my brother name is Ali",
    "im studying in PUCit",
    "i Love coding "
]

# Embed the documents as a batch
res = embedding.embed_documents(doc)

# --- Clean & Informative Printing ---
print(f"Successfully created a matrix of embeddings!")
print(f"Total documents processed: {len(res)}")
print(f"Dimensions per document vector: {len(res[0])}\n")

# Let's inspect the structure of the first document's embedding vector
print("Sample of first document's vector (First 5 numbers):")
print(res[0][:5])