# ChatPromptTemplete we use when we need to send the list of the messages dynamic prompt to the out chatBot

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

# this method is more correct 
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} expert"),
    HumanMessage(content="Explain in simple terms, what is {topic}")
])