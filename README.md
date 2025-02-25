## Web Content Q&A Tool

🔍 About

Web Content Q&A Tool is a LangChain-powered application that extracts and analyzes web content, allowing users to ask questions based on the text of a given URL. It ensures responses are generated purely from the ingested content, making it ideal for research, document analysis, and web-based fact-checking.

Web Content Q&A Tool is a LangChain-powered application that extracts text from web pages and enables users to ask questions based only on the ingested content. It uses OpenAI embeddings, ChromaDB for retrieval, and Streamlit for a user-friendly interface. 🚀

⚡ Features

URL Content Extraction – Fetch and process webpage text automatically.
AI-Powered Q&A – Get answers strictly from the provided content, not external sources.
Efficient Search & Retrieval – Uses ChromaDB for vector-based content search.
User-Friendly UI – Built with Streamlit for seamless interaction.
🚀 Tech Stack

Frontend: Streamlit
AI Engine: LangChain + OpenAI (ChatGPT API)
Storage: ChromaDB (Vector database for retrieval)
💡 Use Cases

Extracting insights from blogs, research papers, or documentation.
Searching and summarizing specific information from lengthy web pages.
Assisting with research without requiring extensive manual reading.

🛠 How to Run

1️⃣ Set Up the Environment

conda create -n aisensy python=3.11 -y
conda activate aisensy

2️⃣ Install Dependencies
Make sure you have a requirements.txt file with all necessary dependencies. Then, run:

pip install -r requirements.txt


3️⃣ Set Up Environment Variables
Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

4️⃣ Run the Application

Depending on whether you're using Streamlit or another framework:

If Streamlit is used:

streamlit run app.py
If Flask/FastAPI is used:

python app.py

5️⃣ Access the Web App

Once running, open the displayed local URL (e.g., http://localhost:8501/ for Streamlit).

