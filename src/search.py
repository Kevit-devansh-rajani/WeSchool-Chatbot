# Step - 4: Search with OpenAI
import os
from dotenv import load_dotenv
from src.vectorstore import FaissVectorStore
import openai

load_dotenv()

class RAGSearch:
    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2",
                 llm_model: str = "gpt-3.5-turbo"):
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)
        # Load or build vectorstore
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from data_loader import load_all_documents
            docs = load_all_documents("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()

        # Initialize OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.llm_model = llm_model
        print(f"[INFO] OpenAI LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        results = self.vectorstore.query(query, top_k=top_k)
        texts = [r["metadata"].get("text", "") for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        if not context:
            return "No relevant documents found."

        prompt = f"""
            You are a helpful AI assistant with knowledge **only about the following context**:

            {context}

            Answer the user's query politely and in a **detailed, well-structured format**. 

            - If the user asks for **records, statistics, or lists** (e.g., placement details, faculty information), provide the answer in **bullet points**.
            - If the user asks a question **outside the context**, politely acknowledge the question and say that you are specialized only for this context. For example:  
            "Thank you for your question! I am specialized in providing information about Weschool. Could you please ask a question related to Weschool?"

            Always ensure your answers are:
            - Clear and informative  
            - Structured (headings, bullet points if needed)  
            - Polite and professional  

            User query: {query}
        """

        response = openai.chat.completions.create(
            model=self.llm_model, 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        return answer
