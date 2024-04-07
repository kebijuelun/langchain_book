# 导入所需的模块和类
from langchain.prompts import (
    ChatMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import AIMessage, HumanMessage

# 定义一个包含变量的提示词模板，其中{name}是一个占位符，这里表示人名
prompt = "{name} 你好，今天由我来给你介绍 LangChain 的使用方式。"

# 使用`from_template`方法创建一个聊天消息的提示词模板，并指定角色为"小明"，使用之前定义的模板
chat_message_prompt = ChatMessagePromptTemplate.from_template(
    role="小明", template=prompt
)

# 通过调用`format`方法传入参数，将输入值应用于聊天消息的提示词模板，生成一个格式化后的聊天消息
print(chat_message_prompt.format(name="小红"))
# -> content='小红 你好，今天由我来给你介绍 LangChain 的使用方式。' additional_kwargs={} role='小明'

# 定义用户提示词模板
human_prompt = "用 {word_count} 个词总结我们到目前为止的对话。"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

# 创建聊天提示词模板，包括对话占位符和用户提示词模板
chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)

# 创建用户消息和 AI 消息
human_message = HumanMessage(content="如何学习编程最好？")
ai_message = AIMessage(
    content="""\
1. 选择一种编程语言：决定要学习的编程语言。

2. 从基础开始：熟悉基本的编程概念，如变量、数据类型和控制结构。

3. 多加练习：最好的学习编程的方式是通过实践经验。
"""
)

# 应用聊天提示词模板，格式化提示词并输出为消息列表
print(
    chat_prompt.format_prompt(
        conversation=[human_message, ai_message], word_count="10"
    ).to_messages()
)
# -> [HumanMessage(content='如何学习编程最好？', additional_kwargs={}), AIMessage(content='1. 选择一种编程语言：决定要学习的编程语言。\n\n2. 从基础开始：熟悉基本的编程概念，如变量、数据类型和控制结构。\n\n3. 多加练习：最好的学习编程的方式是通过实践经验。\n', additional_kwargs={}), HumanMessage(content='用 10 个词总结我们到目前为止的对话。', additional_kwargs={})]
