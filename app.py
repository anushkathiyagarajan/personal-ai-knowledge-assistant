import streamlit as st

from utils.document_loader import extract_text_from_pdfs
from utils.text_splitter import split_text
from utils.embeddings import generate_embeddings
from utils.vector_db import (
    create_vector_store,
    search_similar_chunks
)
from utils.rag_chain import generate_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Personal AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("📂 Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.markdown("---")

    st.subheader("💡 Try asking")

    st.markdown("""
- Who submitted this report?
- What is the project title?
- Summarize the abstract.
- Which dataset was used?
- What technologies were used?
- What is the conclusion?
""")

# ---------------- TITLE ----------------
st.title("🤖 Personal AI Knowledge Assistant")

st.write(
    "Upload your PDF documents and chat with them using Gemini."
)

# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
question = st.chat_input(
    "Ask a question about your PDFs..."
)

# ---------------- MAIN LOGIC ----------------
if question:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    if not uploaded_files:

        response = "⚠️ Please upload at least one PDF."

        with st.chat_message("assistant"):

            st.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    else:

        with st.spinner("🤖 Thinking..."):

            # Extract documents with metadata
            extracted_documents = extract_text_from_pdfs(
                uploaded_files
            )

            # Split into chunks while preserving metadata
            chunked_documents = split_text(
                extracted_documents
            )
            

            # Extract chunk text
            chunk_texts = [
                doc["text"]
                for doc in chunked_documents
            ]

            # Generate embeddings
            embeddings = generate_embeddings(
                chunk_texts
            )

            # Create FAISS index
            index = create_vector_store(
                embeddings
            )

            # Query embedding
            query_embedding = generate_embeddings(
                [question]
            )

            # Retrieve relevant chunks
            distances, indices = search_similar_chunks(
                index,
                query_embedding,
                k=20
            )

            retrieved_chunks = []

            # Always include first chunk
            if len(chunked_documents) > 0:

                retrieved_chunks.append(
                    (0, chunked_documents[0])
                )

            # Add retrieved chunks
            for idx in indices[0]:

                if idx < len(chunked_documents):

                    retrieved_chunks.append(
                        (
                            idx,
                            chunked_documents[idx]
                        )
                    )

            # Remove duplicates
            unique_chunks = {}

            for idx, chunk in retrieved_chunks:

                unique_chunks[idx] = chunk

            retrieved_chunks = list(
                unique_chunks.items()
            )

            # Sort by chunk order
            retrieved_chunks.sort(
                key=lambda x: x[0]
            )

            # Build context
            context = ""

            sources = []

            for idx, chunk in retrieved_chunks:

                context += (
                    chunk["text"] + "\n\n"
                )

                sources.append(
                    (
                        chunk["source"],
                        chunk["page"]
                    )
                )

            # Generate Gemini answer
            response = generate_answer(
                context,
                question
            )

        # Display assistant answer
        with st.chat_message("assistant"):

            st.markdown(response)

            st.markdown("**📄 Sources:**")

            shown = set()

            for source, page in sources:

                if (source, page) not in shown:

                    st.write(
                        f"• {source} (Page {page})"
                    )

                    shown.add(
                        (source, page)
                    )

        # Save assistant message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )