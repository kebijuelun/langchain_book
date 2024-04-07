# 导入所需的库和模块
import os
from git import Repo  # pip install gitpython
from langchain.text_splitter import Language
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser

# 设置 LangChain 存储库的路径（注意需要替换为自己的本地的 langchain 仓库路径）
repo_path = "/home/lwz/langchain"
if not os.path.exists(repo_path):
    # 如果本地没有 langchain 仓库，则从 GitHub 上克隆
    repo = Repo.clone_from(
        "https://github.com/langchain-ai/langchain", to_path=repo_path
    )

# 创建GenericLoader对象，指定加载参数
# GenericLoader用于加载文档，这些文档通常是代码文件
# 以下参数设置了文档加载的配置：
# - repo_path：指定代码存储库的根目录路径
# - glob：使用通配符选择要加载的文件
# - suffixes：指定文件后缀（这里是.py，表示Python源代码文件）
# - parser：指定用于解析文档的语言解析器，这里使用Python解析器
# - parser_threshold：指定解析器的阈值，表示解析的最小文档大小
loader = GenericLoader.from_filesystem(
    repo_path + "/libs/langchain/langchain",
    glob="**/*",
    suffixes=[".py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
documents = loader.load()[
    :100
]  # 加载文档 (注意：为了满足 openai 的 token 数量限制，这里只加载了前 100 个文档，真实场景下建议使用全部文档)
# 上述代码将遍历指定的文件夹（repo_path+"/libs/langchain/langchain"），
# 找到所有以.py为后缀的Python源代码文件，并加载它们作为文档。
# 加载后的文档将存储在documents列表中。

print(len(documents))  # 显示加载的文档数量，注意这个数量可能会随着 langchain 代码库的更新而变化
# -> 1751 (注意：由于在上一代码中只取了前 100 条，所以这里应该会显示 100)

from langchain.text_splitter import RecursiveCharacterTextSplitter

# 创建RecursiveCharacterTextSplitter对象，指定切分参数
# RecursiveCharacterTextSplitter是用于将文档切分成小块的工具。
# 这些小块可以更好地被嵌入和向量化，以供后续的代码理解和分析。
# 在这一步骤中，我们创建了名为python_splitter的RecursiveCharacterTextSplitter对象，
# 并为它指定了以下切分参数：
# - language=Language.PYTHON：指定要切分的文档的语言，这里是Python。
# - chunk_size=800：指定每个切分块的大小，这里是800个字符。
# - chunk_overlap=50：指定切分块之间的重叠量，这有助于确保信息不会在块之间丢失。
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=800, chunk_overlap=50
)

# 切分文档
# 使用python_splitter对象的split_documents方法，将之前加载的文档documents切分成小块（文本块）。
texts = python_splitter.split_documents(documents)
print(len(texts))  # 显示切分后的文本块数量 (注意这个数量可能会随着 langchain 代码库的更新而变化)
# -> 5341 (注意：由于在上一代码中只取了前 1000 条文档，所以这里应该会显示这 1000 条文档切分后的文本块数量)

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# 创建Chroma向量存储对象
# Chroma是一个向量存储工具，用于将文本嵌入（Embed）成向量并进行存储，以便进行语义搜索和检索。
# 在这一步骤中，我们创建了名为db的Chroma向量存储对象，并为其指定以下参数：
# - texts：切分后的文本块列表，这些文本块通常是之前切分过的代码文本。
# - OpenAIEmbeddings(disallowed_special=())：用于嵌入文本的模型，这里使用了OpenAI的嵌入模型。
db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))

# 创建检索器（Retriever）
# 在向量存储对象（Chroma）上创建检索器，以便进行语义检索。
retriever = db.as_retriever(
    search_type="mmr",  # 指定检索类型为"mmr"（最大边际相关性），也可以测试 "similarity"（相似性）
    search_kwargs={"k": 8},  # 指定检索参数，例如返回前8个相关文本
)

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain

# 创建ChatOpenAI聊天模型对象，用于自然语言处理的聊天模型，可以用于提问和获取答案。
# 在这一步骤中，我们创建了名为llm的ChatOpenAI聊天模型对象，并为其指定以下参数：
# - model_name="gpt-4"：指定要使用的聊天模型，这里使用了gpt-4模型。
# llm = ChatOpenAI(model_name="gpt-4")
llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # 如果 openai gpt-4 没有开通则选择 gpt-3.5-turbo

# 创建ConversationSummaryMemory对象，用于存储和管理聊天历史
# 在这一步骤中，我们创建了名为memory的ConversationSummaryMemory对象，并为其指定以下参数：
# - llm=llm：将之前创建的ChatOpenAI聊天模型llm与memory关联，以便存储和管理聊天历史。
# - memory_key="chat_history"：指定用于存储聊天历史的内存键。
# - return_messages=True：设置为True，以便在检索答案时返回聊天消息的详细信息。
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)

# 创建ConversationalRetrievalChain对象，用于处理聊天问题和检索答案
# 在这一步骤中，我们创建了名为qa的ConversationalRetrievalChain对象，并使用from_llm方法进行初始化，指定以下参数：
# - llm=llm：将之前创建的ChatOpenAI聊天模型llm与qa关联，以便处理问题和提供答案。
# - retriever=retriever：用于检索相关文本块的检索器，通常是前面创建的Chroma检索器。
# - memory=memory：用于存储和管理聊天历史的内存工具。
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

# 提出问题并获得答案
# 在这一步骤中，我们提出一个问题并使用qa对象获取答案。
question = "How can I initialize a ReAct agent?"  # 指定要提出的问题
result = qa(question)  # 使用qa对象提问问题，获取答案并将结果存储在result变量中
print(result["answer"])  # 从答案结果中提取具体答案
# -> To initialize a ReAct agent, you can use the `ReActChain` class from the `langchain.agents` module. Here is an example of how to initialize a ReAct agent:
# -> ```
# -> from langchain.agents import ReActChain
# -> agent = ReActChain()
# -> ```
# -> Once initialized, you can use the `agent` object to interact with the ReAct agent and perform actions.
