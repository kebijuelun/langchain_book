import os

import openai

# 从环境变量或秘密管理服务中加载您的API密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

# 创建一个聊天完成请求
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 使用特定的GPT-3.5 Turbo模型
    messages=[{"role": "user", "content": "Hello world"}],  # 用户的消息
)

# 打印模型的回复消息
print(chat_completion["choices"][0]["message"]["content"])
# -> Hello! How can I assist you today?
