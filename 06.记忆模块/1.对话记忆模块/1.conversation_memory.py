import pprint

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

# 创建一个ChatOpenAI实例
llm = ChatOpenAI()
# 定义对话模板
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template("你是一个友善的聊天机器人，正在与用户进行对话。"),
        # 这里的`variable_name`需要与内存中的变量名对应
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)
# 注意，我们使用`return_messages=True`来与MessagesPlaceholder对应
# 注意，`"chat_history"`与MessagesPlaceholder的名称对应。
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# 创建LLMChain实例
conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

# 注意，我们仅传入`question`变量 - `chat_history`会被内存填充
result = conversation({"question": "你好，我今天想和小红去北海公园划船，她是我的好朋友，她有一只可爱的名叫馒头的小狗"})
print(result["text"])
# -> 你好！北海公园划船是一个很好的选择，你和小红还有馒头一定会度过愉快的时光。划船是一个放松身心的活动，你可以欣赏到美丽的风景，同时和好朋友一起享受这个美好的时刻。馒头肯定也会很开心能和你们一起出去玩呢！记得带上狗狗的必需品，比如食物、水和绳子，确保它的安全和舒适。祝你们在北海公园度过一段美好的时光！如果你还有其他问题，我会很乐意回答。

result = conversation({"question": "你还记得小红的狗狗名字是什么吗？"})
print(result["text"])
# -> 是的，小红的狗狗名字是馒头。

# 查看对话返回消息中的记忆信息
pprint.pprint(result["chat_history"])
# -> [HumanMessage(content='你好，我今天想和小红去北海公园划船，她是我的好朋友，她有一只可爱的名叫馒头的小狗', additional_kwargs={}, example=False),
# ->  AIMessage(content='你好！北海公园划船是一个很好的选择，你和小红还有馒头一定会度过愉快的时光。划船是一个放松身心的活动，你可以欣赏到美丽的风景，同时和好朋友一起享受这个美好的时刻。馒头肯定也会很开心能和你们一起出去玩呢！记得带上狗狗的必需品，比如食物、水和绳子，确保它的安全和舒适。祝你们在北海公园度过一段美好的时光！如果你还有其他问题，我会很乐意回答。', additional_kwargs={}, example=False),
# ->  HumanMessage(content='你还记得小红的狗狗名字是什么吗？', additional_kwargs={}, example=False),
# ->  AIMessage(content='是的，小红的狗狗名字是馒头。', additional_kwargs={}, example=False)]
