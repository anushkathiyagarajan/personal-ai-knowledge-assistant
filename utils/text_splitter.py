from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunked_documents = []

    for doc in documents:

        chunks = splitter.split_text(doc["text"])

        for chunk in chunks:

            chunked_documents.append({
                "text": chunk,
                "source": doc["source"],
                "page": doc["page"]
            })

    return chunked_documents