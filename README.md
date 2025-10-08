# 🎓 Weschool Chatbot

<img width="1814" height="857" alt="Screenshot from 2025-10-08 12-17-31" src="https://github.com/user-attachments/assets/d819aa57-579b-460c-8195-b842243b09b8" />

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

# 🚀 Run Weschool Chatbot

1. Clone repo: `git clone https://github.com/yourusername/weschool-chatbot.git && cd weschool-chatbot`  
2. Create venv & activate: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)  
3. Install deps: `pip install -r requirements.txt`  
4. Add OpenAI key in `.env`: `OPENAI_API_KEY=sk-your-api-key`  
5. Place PDFs in `data/` folder  
6. Run app: `streamlit run app.py`  
7. Ask questions in the chat interface!
