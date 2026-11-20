from langchain_community.document_loaders import TextLoader

loader = TextLoader('tarok.txt') #only one file load

document = loader.load()

print(len(document))
print(document[0].page_content)
