import os
import openai

# 从环境变量或秘密管理服务中加载您的API密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

# 创建一个聊天完成请求
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 使用特定的GPT-3.5 Turbo模型
    temperature=0,  # 温度参数控制生成的文本的多样性，0表示生成的文本更加确定性
    messages=[{"role": "user", "content": "你是谁？"}],  # 用户的消息
)

# 打印模型的回复消息
print(chat_completion["choices"][0]["message"]["content"])
# -> 我是一个AI助手，被称为OpenAI。我被设计用来回答各种问题和提供帮助。


from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# 导入自定义的ChatOpenAI类以及消息类型
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# 使用自定义聊天模型生成回复
result = chat([HumanMessage(content="你是谁？")])  # 用户的消息内容
print(result.content)  # 打印模型的回复消息
# -> 我是一个AI助手，被称为OpenAI。我被设计用来回答各种问题和提供帮助。
