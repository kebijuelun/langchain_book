# 导入所需的模块
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# 创建一个系统消息的提示词模板，使用给定的模板和变量
template = "你是一个翻译从{input_language}到{output_language}的有帮助的助手。"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 创建一个用户消息的提示词模板，使用给定的模板和变量
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 创建一个聊天提示词模板，由系统消息和用户消息组成
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# 将输入值应用于聊天提示词模板，生成聊天消息的列表 (输出为 message 格式)
print(
    chat_prompt.format_prompt(
        input_language="英文", output_language="中文", text="I love programming."
    ).to_messages()
)
# -> [SystemMessage(content='你是一个翻译从英文到中文的有帮助的助手。', additional_kwargs={}), HumanMessage(content='I love programming.', additional_kwargs={})]

# 将输入值应用于聊天提示词模板，生成格式化的聊天消息字符串 (输出为 string 格式)
print(
    chat_prompt.format_prompt(
        input_language="英文", output_language="中文", text="I love programming."
    ).to_string()
)
# -> System: 你是一个翻译从英文到中文的有帮助的助手。
# -> Human: I love programming.
