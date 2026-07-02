from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Initialize the local embedding model correctly (Removed invalid parameter)
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

document = [
    "Aerospace engineering focuses on the design, development, and testing of aircraft and spacecraft.",
    "Cloud computing enables scalable, on-demand access to shared computer processing resources and data storage over the internet.",
    "Mass communication explores how information is broadcasted and consumed through journalism, digital media, and public relations.",
    "Cardiology is a specialized medical field dedicated to diagnosing and treating disorders of the human heart and blood vessels.",
    "Renewable energy systems harness natural resources like sunlight, wind, and water to generate sustainable electrical power."
]


query = 'How does broadcasting information via digital media work?'

# 2. Changed async calls (aembed) to standard synchronous calls (embed)
doc_embd = embedding.embed_documents(document)
query_embd = embedding.embed_query(query)

# 3. Calculate cosine similarity
# Wrapping query_embd inside [query_embd] turns the 1D list into a 2D array matrix required by sklearn
score = cosine_similarity([query_embd], doc_embd)[0] 

# 4. Find the highest matching document
index, top_score = sorted(list(enumerate(score)), key=lambda x: x[1])[-1] 

# 5. Print results
print("Best Match Document:")
print(document[index])
print(f"Similarity Score is: {top_score:.4f}")

print ("similarity report completed ")