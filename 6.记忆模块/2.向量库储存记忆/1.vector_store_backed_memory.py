import faiss
from langchain.chains import ConversationChain
from langchain.docstore import InMemoryDocstore
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS

# 设置 OpenAIEmbeddings 的维度
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
embedding_fn = OpenAIEmbeddings().embed_query
vectorstore = FAISS(embedding_fn, index, InMemoryDocstore({}), {})

# 在实际使用中，您可以将 `k` 设置为较大的值，但我们这里将 k 设置为 1，以展示向量查找仍然返回语义相关信息
retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))
memory = VectorStoreRetrieverMemory(retriever=retriever)

# 将相关信息从对话或工具保存到记忆中
memory.save_context({"input": "我最喜欢的食物是披萨"}, {"output": "这个我知道"})
memory.save_context({"input": "我最喜欢的运动是足球"}, {"output": "..."})
memory.save_context({"input": "我不喜欢凯尔特人队"}, {"output": "好的"})  #

print(memory.load_memory_variables({"prompt": "我应该看哪种运动？"})["history"])
# -> input: 我最喜欢的运动是足球
# -> output: ...

llm = OpenAI(temperature=0)  # 可以是任何有效的 LLM
_DEFAULT_TEMPLATE = """以下是人类和 AI 之间友好对话的一部分。AI 健谈，会从其上下文中提供大量具体细节。如果 AI 不知道问题的答案，它会真实地表示不知道。

先前对话中的相关片段：
{history}

（如果不相关，您无需使用这些信息）

当前对话：
人类：{input}
AI："""
PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=_DEFAULT_TEMPLATE
)
conversation_with_summary = ConversationChain(
    llm=llm,
    prompt=PROMPT,
    # 为测试目的，设置一个非常低的 max_token_limit
    memory=memory,
    verbose=True,
)
conversation_with_summary.predict(input="嗨，我叫 Perry，你好吗？")
# -> > Entering new ConversationChain chain...
# -> Prompt after formatting:                                                                                             [40/121]
# -> 以下是人类和 AI 之间友好对话的一部分。AI 健谈，会从其上下文中提供大量具体细节。如果 AI 不知道问题的答案，它会真实地表示不知道。

# -> 先前对话中的相关片段：
# -> input: 我最喜欢的食物是披萨
# -> output: 这个我知道

# -> （如果不相关，您无需使用这些信息）

# -> 当前对话：
# -> 人类：嗨，我叫 Perry，你好吗？
# -> AI：

# -> > Finished chain.
# -> 你好，Perry，很高兴认识你！我叫 AI，我可以回答你的问题，也可以和你聊天。你想问我什么？

# 这里，与足球相关的内容被提取出来
conversation_with_summary.predict(input="我最喜欢的运动是什么？")
# -> > Entering new ConversationChain chain...
# -> Prompt after formatting:
# -> 以下是人类和 AI 之间友好对话的一部分。AI 健谈，会从其上下文中提供大量具体细节。如果 AI 不知道问题的答案，它会真实地表示不知道。

# -> 先前对话中的相关片段：
# -> input: 我最喜欢的运动是足球
# -> output: ...

# -> （如果不相关，您无需使用这些信息）

# -> 当前对话：
# -> 人类：我最喜欢的运动是什么？
# -> AI：

# -> > Finished chain.
# -> 您最喜欢的运动是足球，对吗？您是否喜欢足球的竞技性？或者您更喜欢踢足球的乐趣？

# 尽管语言模型是无状态的，但由于提取了相关的记忆，它可以“推理”时间。
# 在一般情况下，为记忆和数据加上时间戳是很有用的，以便让代理程序确定时间上的相关性
conversation_with_summary.predict(input="我最喜欢的食物是什么？")
# -> > Entering new ConversationChain chain...
# -> Prompt after formatting:
# -> 以下是人类和 AI 之间友好对话的一部分。AI 健谈，会从其上下文中提供大量具体细节。如果 AI 不知道问题的答案，它会真实地表示不知道。

# -> 先前对话中的相关片段：
# -> input: 我最喜欢的食物是披萨
# -> output: 这个我知道

# ->（如果不相关，您无需使用这些信息）

# -> 当前对话：
# -> 人类：我最喜欢的食物是什么？
# -> AI：

# -> > Finished chain.
# -> 您最喜欢的食物是披萨吗？
