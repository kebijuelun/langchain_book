### 基础调用样例
# 导入 OpenAI 对话模型类
from langchain.chat_models import ChatOpenAI

# 导入消息类型
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# 定义 OpenAI 对话模型
chat = ChatOpenAI(temperature=0)

# 给定人类指令消息，调用 OpenAI 对话模型获取对话模型输出
result = chat(
    [
        HumanMessage(
            content="Translate this sentence from English to Chinese. I love programming."
        )
    ]
)
print(result.content)
# 我喜欢编程。

### 多 Message 组合调用对话模型
# OpenAI 支持输入 SystemMessage 消息给对话系统进行额外的定义或约束
messages = [
    SystemMessage(
        content='You are a helpful assistant that translates English to Chinese, and you will add a "中文翻译结果: " before each reply text.'
    ),
    HumanMessage(content="I love programming."),
]
result = chat(messages)
print(result.content)
# -> 中文翻译结果: 我喜欢编程

### 批量对话
batch_messages = [
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to Chinese."
        ),
        HumanMessage(content="I love programming."),
    ],
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to Chinese."
        ),
        HumanMessage(content="I love artificial intelligence."),
    ],
]
result = chat.generate(batch_messages)
print(result.generations)
# -> [[ChatGeneration(text='我喜欢编程。', generation_info=None, message=AIMessage(content='我喜欢编程。', additional_kwargs={}))], [ChatGeneration(text='我喜欢人工智能。', generation_info=None, message=AIMessage(content='我喜欢人工智能。', additional_kwargs={}))]]
print(result.llm_output)
# -> {'token_usage': {'prompt_tokens': 57, 'completion_tokens': 19, 'total_tokens': 76}, 'model_name': 'gpt-3.5-turbo'}

### 多轮对话
messages = [
    SystemMessage(content="你是一个乐于助人的人工智能助手。"),
    HumanMessage(content="哪个国家赢得了 2018 年世界杯冠军?"),
    AIMessage(content="2018年世界杯冠军是法国。"),
    HumanMessage(content="比赛是在哪个国家举办的?"),
]
result = chat(messages)
print(result.content)
# -> 2018年世界杯比赛是在俄罗斯举办的。
