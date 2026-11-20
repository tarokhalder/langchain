from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
     "https://codeforces.com/problemset/problem/2290/H"
)

document = loader.load()

print(document[0].page_content)
