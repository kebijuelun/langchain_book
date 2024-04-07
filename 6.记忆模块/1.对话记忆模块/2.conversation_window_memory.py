import pprint

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
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
        SystemMessagePromptTemplate.from_template(
            "你是一个友善的聊天机器人，对于用户的问题会直接回复答案，不会说过多的废话，也不会反问用户问题。"
        ),
        # 这里的`variable_name`需要与内存中的变量名对应
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)
# 注意，我们使用`return_messages=True`来与MessagesPlaceholder对应
# 注意，`"chat_history"`与MessagesPlaceholder的名称对应。
memory = ConversationBufferWindowMemory(
    memory_key="chat_history", return_messages=True, k=1
)
# 创建LLMChain实例
conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

# 注意，我们仅传入`question`变量 - `chat_history`会被内存填充
result = conversation({"question": "你好，我今天想和小红去北海公园划船，她是我的好朋友，她有一只可爱的名叫馒头的小狗"})
print(result["text"])
# -> 你好！北海公园是一个很不错的选择，划船是一个很好的活动。希望你和小红能够度过愉快的时光。馒头一定是个可爱的小狗。祝你们玩得开心

result = conversation({"question": "你还记得我今天想和谁去北海公园划船吗？"})
print(result["text"])
# -> 是的，小红的狗狗名字是馒头。

result = conversation({"question": "你说对了，真聪明"})
print(result["text"])
# -> 谢谢夸奖！如果你还有其他问题，我会尽力回答。

# 查看对话返回消息中的记忆信息
pprint.pprint(result["chat_history"])
# -> [HumanMessage(content='你还记得我今天想和谁去北海公园划船吗？', additional_kwargs={}, example=False), AIMessage(content='你今天想和小红去北海公园划船。', additional_kwargs={}, example=False)]

result = conversation({"question": "你还记得小红的小狗叫什么名字吗？"})
print(result["text"])
# -> 抱歉，作为一个聊天机器人，我没有记忆功能，无法记得小红的小狗叫什么名字。
