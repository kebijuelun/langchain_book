# 导入所需的模块和类
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.chains import LLMChain

# 创建聊天提示模板，指定要获取关于的主题
prompt = ChatPromptTemplate.from_template("给我一个关于{topic}的一句话介绍")

# 创建ChatOpenAI模型实例
model = ChatOpenAI(temperature=0)

# 创建输出解析器实例
output_parser = StrOutputParser()

# 创建LLMChain链，将聊天提示、模型和输出解析器组合在一起
chain = LLMChain(prompt=prompt, llm=model, output_parser=output_parser)

# 运行链，并指定主题为"大语言模型"
out = chain.run(topic="大语言模型")
print(out)
# -> 大语言模型是一种基于深度学习的人工智能技术，能够自动学习和生成自然语言文本，具有广泛的应用领域，如机器翻译、文本生成和对话系统等

# 使用 LangChain Expression Language（LCEL）创建链
lcel_chain = prompt | model | output_parser

# 运行链，并通过字典传递主题为"大语言模型"
out = lcel_chain.invoke({"topic": "大语言模型"})
print(out)
# -> 大语言模型是一种基于深度学习的人工智能技术，能够自动学习和生成自然语言文本，具有广泛的应用领域，如机器翻译、文本生成和对话系统等
