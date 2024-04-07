from langchain import PromptTemplate

# 定义提示词模板
template = """
我希望你能担任新公司的命名顾问。
一个制造{product}的公司取什么好名字呢？
"""

# 创建提示词模板实例
prompt = PromptTemplate(
    input_variables=["product"],  # 指定模板中的变量
    template=template,  # 使用定义的模板字符串
)

# 使用模板实例进行格式化，替换占位符为具体的值
generated_prompt = prompt.format(product="彩色袜子")

# 打印生成的提示文本
print(generated_prompt)
# -> 我希望你能担任新公司的命名顾问。
# -> 一个制造彩色袜子的公司取什么好名字呢？
