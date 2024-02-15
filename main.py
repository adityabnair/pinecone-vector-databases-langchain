import os
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import Pinecone as PineconeStore
from langchain.chains import RetrievalQA
from pinecone import Pinecone, ServerlessSpec

load_dotenv()  # take environment variables from .env.

pc = Pinecone(api_key="PINECONE_API_KEY")

if __name__ == "__main__":
    print("Hello, World!")
    loader = TextLoader(
        r"D:\IDrive-Sync\vector-db\mediumblogs\mediumblog1.txt", encoding="UTF-8"
    )
    document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    docsearch = PineconeStore.from_documents(
        texts, embeddings, index_name="medium-blogs-embedding-index"
    )  # storing vectors and chunks in the pinecone serverless index (eucidiean)
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo"),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
    )
    query = "What is a vector DB? Give me a 15 word answer for a beginner"
    result = qa({"query": query})
    print(result)
