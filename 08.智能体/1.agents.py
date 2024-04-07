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

# 第2步：创建提示
# 导入所需的库或模块
from langchain.schema import SystemMessage

# 创建一个系统消息对象，用于设定智能体的背景或性能期望
system_message = SystemMessage(
    content="You are a very powerful assistant, but bad at calculating word lengths."
)

# 使用 OpenAIFunctionsAgent 的 create_prompt 函数生成提示
prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message)


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

# 创建一个 AgentExecutor 对象，该对象代表了代理的运行时环境
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# 第5步：测试智能体
agent_executor.run("how many letters in the word educa?")
#   > Entering new AgentExecutor chain...
#     Invoking: `get_word_length` with `{'word': 'educa'}`
#     5
#     There are 5 letters in the word "educa".
#     > Finished chain.
#     'There are 5 letters in the word "educa".'
