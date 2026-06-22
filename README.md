
# 🤖 Personal AI Knowledge Assistant

An AI-powered document question-answering system that allows users to upload PDF documents and chat with them using Retrieval-Augmented Generation (RAG).

---

## ✨ Features

- 📄 Upload one or multiple PDF documents
- 🔍 Extract text from PDFs
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- ⚡ Store and retrieve chunks using FAISS
- 🤖 Answer questions using Google Gemini
- 💬 ChatGPT-style conversation interface
- 📚 Maintain chat history
- 📌 Suggested questions sidebar
- 🛡️ Graceful handling of Gemini API quota limits

---

## 🏗️ System Architecture

PDF Upload
↓
Text Extraction
↓
Text Chunking
↓
Sentence Embeddings
↓
FAISS Vector Store
↓
Relevant Chunk Retrieval
↓
Gemini (RAG)
↓
Answer Generation

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### AI & NLP
- Google Gemini API
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- FAISS

### PDF Processing
- PyPDF

### Environment Management
- python-dotenv

---

## 📂 Project Structure

```
mini 5/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── utils/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── prompts.py
│   └── rag_chain.py
│
└── venv311/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
cd mini-5
```

### Create Virtual Environment

```bash
py -3.11 -m venv venv311
```

### Activate Virtual Environment

Windows:

```bash
venv311\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Generate your API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 💡 Example Questions

- Who submitted this project report?
- What is the title of the project?
- Summarize the abstract.
- Which dataset was used?
- What technologies were used?
- What is the conclusion?
- Generate viva questions from this report.
- Explain this project in simple language.

---

## 🚀 Future Enhancements

- Page-level citations
- PDF preview
- Download answers as PDF/Word
- Voice input/output
- Multi-document comparison
- Local LLM fallback
- Advanced hybrid retrieval
- Authentication and user accounts

---

## 📸 Screenshots

Add screenshots of:

- Chat Interface
- PDF Upload
- Question Answering
- Sidebar Features

---

## 👩‍💻 Author

Developed as part of an AI-powered document understanding project using Retrieval-Augmented Generation (RAG).

---

## 📜 License

This project is intended for educational and learning purposes.
<<<<<<< HEAD
=======
=======
# personal-ai-knowledge-assistant

>>>>>>> e269a96461b4a30e451e00bbb51a7b50709c5a52
