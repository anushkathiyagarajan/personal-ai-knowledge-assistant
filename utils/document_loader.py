from pypdf import PdfReader


def extract_text_from_pdfs(uploaded_files):

    documents = []

    for pdf in uploaded_files:

        reader = PdfReader(pdf)

        for page_num, page in enumerate(reader.pages, start=1):

            page_text = page.extract_text()

            if page_text:
                documents.append({
                    "text": page_text,
                    "source": pdf.name,
                    "page": page_num
                })

    return documents