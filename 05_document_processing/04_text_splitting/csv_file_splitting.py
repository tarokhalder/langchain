from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = CSVLoader("Housing.csv")

document = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400 ,
    chunk_overlap = 100
)

chunks = splitter.split_documents(document)

for chunk in chunks:
    print(chunk.metadata)
    print(chunk.page_content)
