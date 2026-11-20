from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader('tarok.txt')

document = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=100
)

chunks = splitter.split_documents(document)

print(len(chunks))

for chunk in chunks:
    print(chunk.page_content)
    print(chunk.metadata)
