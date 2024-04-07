# 终端配置 ANTHROPIC_API_KEY 环境变量
# export ANTHROPIC_API_KEY=xxx

# 导入 Anthropic 对话模型类
from langchain.chat_models import ChatAnthropic

# 导入消息类型
from langchain.schema import HumanMessage

# 定义 Anthropic 对话模型
chat = ChatAnthropic()

# 给定人类指令消息，调用 Anthropic 对话模型获取对话模型输出
messages = [
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    )
]
result = chat(messages)
print(result.content)
# -> J'aime programmer.
