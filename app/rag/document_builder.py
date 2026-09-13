from langchain_core.documents import Document

def create_documents(chunks:list[str])->list[Document]:
    documents = []

    for index , chunk in enumerate(chunks):
        document = Document(
            page_content = chunk,
            metadata = {
                "chunk_id":index
            }
        )

        documents.append(document)

    return documents