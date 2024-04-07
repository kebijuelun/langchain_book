from langchain import LLMChain, OpenAI, PromptTemplate

# 定义模板字符串，包含问题和回答的格式
template = """Question: {question}

Answer: Let's think step by step."""

# 创建一个PromptTemplate实例，指定模板字符串和输入变量为"question"
prompt = PromptTemplate(template=template, input_variables=["question"])

# 创建一个LLMChain实例，指定PromptTemplate、语言模型实例和verbose为True
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

# 将LLMChain实例保存为JSON文件
llm_chain.save("llm_chain.json")

# 从JSON文件中加载LLMChain实例
from langchain.chains import load_chain

chain = load_chain("llm_chain.json")

# 使用加载的链式结构进行运行，传入问题"whats 2 + 2"
result = chain.run("whats 2 + 2")
# -> > Entering new  chain...
# -> Prompt after formatting:
# -> Question: whats 2 + 2
# -> Answer: Let's think step by step.
# -> > Finished chain.

# 打印运行结果
print(result)
# -> 2 + 2 = 4
