import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


import chromadb.api


def load_documents(url):
    loader = WebBaseLoader(web_paths=[url], bs_kwargs=dict(parse_only=bs4.SoupStrainer("main")))
    return loader.load()

def setup_retrieval_chain(docs, openai_api_key):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_db = Chroma.from_documents(split_docs, embeddings)
    
    template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Write with simple language. Write at least least 5 sentences.

    {context}

    Question: {question}

    Helpful Answer:"""
    
    prompt_template = PromptTemplate.from_template(template)
    
    
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    
    st.success(retriever) # remove
    
    llm = ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0,openai_api_key=openai_api_key)
    
    qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt_template
    | llm
    | StrOutputParser()
    )   
    return qa_chain

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def main():
    st.title("Web Content Q&A Tool")
    _ = load_dotenv(find_dotenv())
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("Missing OpenAI API Key")
        return
    
    page_url = st.text_input("Enter the URL to analyze:")
    if st.button("Load and Process Content") and page_url:
        with st.spinner("Loading content..."):
            docs = load_documents(page_url)
            st.success("Content loaded successfully!")
            chromadb.api.client.SharedSystemClient.clear_system_cache()
            qa_chain = setup_retrieval_chain(docs, openai_api_key)
            st.session_state.qa_chain = qa_chain
    
    if "qa_chain" in st.session_state:
        query = st.text_input("Ask a question about the content:")
        if st.button("Get Answer") and query:
            response = st.session_state.qa_chain.invoke(query)
            st.write(f"**Answer:** {response}")
    
if __name__ == "__main__":
    main()
