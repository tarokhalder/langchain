from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()

llm = ChatGroq(
    model ="openai/gpt-oss-20b",
    max_tokens = 500,
    temperature= 0.7
)

loader = TextLoader('tarok.txt')

document = loader.load()

ans = llm.invoke(
    f"Make 5 questions based on the following document:\n\n{document[0].page_content}"
)

print(ans.content)


