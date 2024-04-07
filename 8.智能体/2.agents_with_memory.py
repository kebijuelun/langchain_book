# 第1步：定义工具
# 导入所需的库或模块
from langchain.agents import tool


# 使用装饰器 @tool 来定义一个自定义工具函数
@tool
def get_word_length(word: str) -> int:
    """返回单词的长度"""
    return len(word)


# 创建一个工具列表，将自定义工具函数添加到其中
tools = [get_word_length]


from langchain.agents import OpenAIFunctionsAgent
from langchain.prompts import MessagesPlaceholder

# 第2步：创建提示
# 导入所需的库或模块
from langchain.schema import SystemMessage

# 创建一个系统消息对象，用于设定智能体的背景或性能期望
system_message = SystemMessage(
    content="You are a very powerful assistant, but bad at calculating word lengths."
)

# 定义一个记忆键（MEMORY_KEY），用于在提示中引用记忆位置，标识智能体中的聊天历史或对话记忆。
MEMORY_KEY = "chat_history"

# 使用 OpenAIFunctionsAgent 的 create_prompt 函数创建提示（prompt）
prompt = OpenAIFunctionsAgent.create_prompt(
    system_message=system_message,
    extra_prompt_messages=[
        MessagesPlaceholder(variable_name=MEMORY_KEY)
    ],  # 将一个消息占位符添加到额外提示消息中
)

# 第3步：创建智能体
# 导入所需的库或模块
from langchain.chat_models import ChatOpenAI

# 创建 ChatOpenAI 实例，设置温度（temperature）为 0
# temperature 参数通常用于控制生成文本的多样性。将温度设置为较低的值（例如 0）会使生成的文本更加确定和一致，而将其设置为较高的值则会增加生成文本的随机性。
llm = ChatOpenAI(temperature=0)

# 使用 OpenAIFunctionsAgent 类创建一个智能体对象
agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)


# 第4步：创建智能体执行器
# 导入所需的库或模块
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory

# 创建一个 ConversationBufferMemory 对象
memory = ConversationBufferMemory(
    memory_key=MEMORY_KEY, return_messages=True  # 指定记忆对象的键，以便在后续代码中与记忆位置匹配
)

# 创建一个 AgentExecutor 对象，该对象代表了代理的运行时环境
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)


# 第5步：测试智能体
agent_executor.run("how many letters in the word educa?")
agent_executor.run("is that a real word?")
