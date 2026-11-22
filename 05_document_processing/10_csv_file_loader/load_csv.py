from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    "Housing.csv"
)

content = loader.load()

print(content[0].page_content)
