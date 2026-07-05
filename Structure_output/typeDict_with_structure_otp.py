from typing import TypedDict,Annotated,Optional
from langchain_ollama import ChatOllama

model=ChatOllama(
    temperature=0.7,
    model="llama3.2"
)

class Review(TypedDict):
    summary: Annotated[str,'A breif summary of the review']   # guiding out model exactly what to do 
    sentiment: Annotated [str, "Return sentiment of the review either negative, positive or neutral"]
    key_theme:Annotated[list[str],"write down the all the key themes discussed in the review in list"  ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the gons inside a list"]
    
structured_model=model.with_structured_output(Review)

review="""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
pill to swallow.

Pros :
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors I"""
result=structured_model.invoke(review)

print(result)
print("\nSummary:", result["summary"])
print("Sentiment:", result["sentiment"]) 