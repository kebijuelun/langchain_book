from pprint import pprint

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader  # 导入WebBaseLoader用于加载网页文档
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import (
    ConversationBufferMemory,
)  # 导入ConversationBufferMemory用于创建记忆
from langchain.prompts.prompt import PromptTemplate
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)  # 导入RecursiveCharacterTextSplitter用于拆分文档
from langchain.vectorstores import Chroma

# 使用WebBaseLoader加载维基百科上的科比·布莱恩特页面
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Kobe_Bryant")
data = loader.load()

# 使用RecursiveCharacterTextSplitter拆分文档成多个片段
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# 创建ChatOpenAI实例
llm = ChatOpenAI()

# 使用Chroma和OpenAIEmbeddings将文档转化为向量
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

# 创建ConversationBufferMemory，用于存储聊天记录
memory = ConversationBufferMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)

# 定义一个模板，用于将用户的问题重新表述成独立问题
_template = """给定以下对话和后续问题，请将后续问题重新表述为一个独立的问题，使用其原始语言。

聊天记录：
{chat_history}
后续输入：{question}
独立问题："""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

# 使用Chroma检索器创建ConversationalRetrievalChain
retriever = vectorstore.as_retriever()
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory,
    verbose=True,
    condense_question_prompt=CONDENSE_QUESTION_PROMPT,
)

# 查询科比获得多少次NBA总冠军
response = qa("科比拿过多少次NBA总冠军？")
print(response["answer"])
# -> 科比·布莱恩特（Kobe Bryant）在NBA职业生涯中共获得了5次总冠军。

# 查询科比是哪年退役的
response = qa("科比是哪年退役的？")
print(response["answer"])
# -> 科比在2016年退役的。
