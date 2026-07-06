from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

# Define what fields you want
response_schemas = [
    ResponseSchema(name="facts", description="List of 5 interesting facts", type="list"),
    ResponseSchema(name="summary", description="One sentence summary", type="string"),
    ResponseSchema(name="difficulty", description="Easy, Medium, or Hard", type="string")
]

# Create Parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Create Prompt
prompt = PromptTemplate(
    template="""Give information about {topic}.
    
    {format_instructions}""",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

model = ChatOllama(model="llama3.2", temperature=0)

chain = prompt | model | parser

result = chain.invoke({"topic": "Black Hole"})

print(result)