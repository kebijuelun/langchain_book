import getpass
import os

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

raw_documents = TextLoader("./state_of_the_union.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

db = FAISS.from_documents(documents, OpenAIEmbeddings())

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)
print(docs[0].page_content)

embedding_vector = embeddings.embed_query(query)
docs = db.similarity_search_by_vector(embedding_vector)
print(docs)
