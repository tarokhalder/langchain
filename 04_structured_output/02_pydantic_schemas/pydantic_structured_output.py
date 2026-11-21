from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field


class Question(BaseModel):
    problem: str = Field(
        description="The actual programming problem statement"
    )

    time_limit: str = Field(
        description="Time limit for the problem",
        max_length=10,
        min_length=2
    )

    space_limit: str = Field(
        description="Memory limit for the problem",
        max_length=10,
        min_length=2
    )


class Solution(BaseModel):
    approach: str = Field(
        description="Explain the algorithmic approach, such as Greedy or Dynamic Programming"
    )

    solution: str = Field(
        description="Explain the solution with Python code and complexity analysis"
    )


class Problem(BaseModel):
    question: Question
    answer: Solution


load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

model = llm.with_structured_output(Problem)

ans = model.invoke(
    "Give me a Python programming problem and its solution."
)

print(ans)

