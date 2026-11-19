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
          description= "You have to explain a python problem" ,
          min_length=10
     )
     solution : str = Field(
          description="you have to make a solution based on problem" ,
          max_length= 5000
     )
     
model = llm.with_structured_output(Output)
output = model.invoke("Teach me a python Programming Problem")

json_output = output.model_dump_json(indent = 4)

print(json_output)
