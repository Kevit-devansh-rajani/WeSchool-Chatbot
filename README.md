# 🎓 Weschool Chatbot

**A Retrieval-Augmented Generation (RAG) Chatbot** for Weschool – the Best Business School in India.  
This chatbot allows users to ask questions about Weschool’s programs, faculty, placements, and other details. It retrieves information from documents and generates detailed, structured answers using AI.

---

## 🌟 Features

- **RAG Pipeline:** Combines vector search (FAISS) with LLMs to answer queries based on documents.  
- **Multilingual Support:** Uses `sentence-transformers` for embeddings.  
- **Interactive Chat UI:** Streamlit app with conversation-style interface.  
- **Structured Responses:** Bullet points for records (placements, faculty), headings for sections.  
- **Out-of-Context Handling:** Politely handles queries outside available documents.  
- **Offline Embeddings:** FAISS stores embeddings locally to avoid recomputation.

---

## 🛠️ Technologies Used

| Module          | Technology                  | Purpose |
|-----------------|----------------------------|---------|
| PDF Loader      | `pdfplumber`               | Extract text from PDFs |
| Embeddings      | `sentence-transformers`    | Convert text chunks to vector embeddings |
| Vector Search   | `faiss-cpu`                | Efficient similarity search of embeddings |
| LLM             | OpenAI GPT / HuggingFace Transformers | Generate structured answers |
| Web UI          | `Streamlit`                | Interactive chatbot interface |
| Environment     | `python-dotenv`            | Load API keys and configuration |

---
