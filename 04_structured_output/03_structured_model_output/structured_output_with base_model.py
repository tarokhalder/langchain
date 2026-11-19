from langchain_groq import ChatGroq
from pydantic import BaseModel , Field
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
     model="openai/gpt-oss-120b",
     temperature=0.9 ,

)

class Output(BaseModel):
     problem : str =  Field(
          description= "You have to explain a python problem"
     )
     solution : str = Field(
          description="you have to make a solution based on problem"
     )
     
model = llm.with_structured_output(Output)
output = model.invoke("Teach me a python Programming Problem")

print(output.problem)

print(" ")
print(output.solution)
