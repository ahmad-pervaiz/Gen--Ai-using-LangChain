from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


llm= OpenAI(model='gpt-4o-mini')
res=llm.invoke("what is the capital Pakistan")
print(res)