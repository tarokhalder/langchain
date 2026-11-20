from langchain_core.documents import Document

doc = Document(
    page_content="Machine Learning is a subset of AI.",
    metadata={
        "source": "ml.txt",
        "topic": "Machine Learning"
    }
)

print(doc.page_content)
print(doc.metadata)
