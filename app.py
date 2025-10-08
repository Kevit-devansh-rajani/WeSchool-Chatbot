# app.py - Attractive Weschool Chatbot
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
import streamlit as st

# Page Config
st.set_page_config(page_title="🎓 Weschool Chatbot", layout="wide")

# Title
st.title("🎓 Weschool Chatbot")
st.markdown("Ask anything about **Weschool** - the Best Business School in India.")

# Initialize Modules
if "rag_search" not in st.session_state:
    st.session_state.rag_search = RAGSearch()

rag_search = st.session_state.rag_search

# Load FAISS vectors (if needed)
if "store_loaded" not in st.session_state:
    store = FaissVectorStore("faiss_store")
    store.load()
    st.session_state.store_loaded = True

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# Chat Input
user_input = st.chat_input("Type your question here...")
if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Weschool Assistant is thinking..."):
        answer = rag_search.search_and_summarize(user_input, top_k=3)

    # Show assistant message
    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("---")
st.markdown("Powered by **RAG + OpenAI GPT** | Made for **Weschool** 🎓")
