from langchain import HuggingFaceHub, LLMChain, PromptTemplate

# 定义语言模型
repo_id = "google/flan-t5-xl"  # huggingface 上的 repo id, 一般以模型名称进行命名, 在 https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads 中可以查看更多的模型选项
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64})

# 定义输入提示词模板
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# 基于语言模型获取输出文本
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "Who won the FIFA World Cup in the year 1994? "
print(llm_chain.run(question))
# -> The FIFA World Cup is a football tournament that is played every 4 years. The year 1994 was the 44th FIFA World Cup. The final answer: Brazil.
