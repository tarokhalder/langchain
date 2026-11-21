from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('loader.pdf')

document = loader.load()

print(document[1].page_content)
