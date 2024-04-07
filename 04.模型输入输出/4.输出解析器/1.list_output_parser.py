from langchain.llms import OpenAI  # 导入语言模型类
from langchain.output_parsers import CommaSeparatedListOutputParser  # 导入逗号分隔列表输出解析器类
from langchain.prompts import PromptTemplate  # 导入提示模板类

output_parser = CommaSeparatedListOutputParser()  # 创建逗号分隔列表输出解析器对象

format_instructions = output_parser.get_format_instructions()  # 获取输出解析器的格式说明
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

model = OpenAI(temperature=0)  # 创建语言模型对象，设置温度参数为0

_input = prompt.format(subject="fruit")  # 格式化提示模板，将主题设置为 "fruit"
print(_input)
# -> List five fruit.
# -> Your response should be a list of comma separated values, eg: `foo, bar, baz`

output = model(_input)  # 调用语言模型，传入输入对象，获取输出结果
print(output)
# -> Apple, Banana, Orange, Strawberry, Watermelon
