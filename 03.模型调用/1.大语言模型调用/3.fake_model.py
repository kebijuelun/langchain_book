# 导入 LangChain 封装的 FakeListLLM 库
from langchain.llms.fake import FakeListLLM

# 定义虚假模型的文本输出
responses = [
    "test1",
    "test2",
]

# 定义虚假模型
llm = FakeListLLM(responses=responses)

# 调用虚假模型，此时模型返回值就是 responses 中的定义文本输出，与模型函数输入无关
print(llm(""))
# -> test1
print(llm(""))
# -> test2
