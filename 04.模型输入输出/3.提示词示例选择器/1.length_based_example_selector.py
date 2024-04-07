from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

# 这是一些虚构的任务示例，用于创建反义词。
examples = [
    {"input": "快乐", "output": "悲伤"},
    {"input": "高", "output": "矮"},
    {"input": "充满活力", "output": "倦怠"},
    {"input": "晴朗", "output": "阴沉"},
    {"input": "有风的", "output": "平静"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="输入：{input}\n输出：{output}",
)
example_selector = LengthBasedExampleSelector(
    # 可供选择的例子集合。
    examples=examples,
    # 用于格式化例子的 PromptTemplate。
    example_prompt=example_prompt,
    # 格式化后的例子的最大长度。
    # 长度由下面的 get_text_length 函数测量。
    max_length=35,
    get_text_length=lambda x: len(x),
)
dynamic_prompt = FewShotPromptTemplate(
    # 提供 ExampleSelector 而不是例子集合。
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="输入：{adjective}\n输出：",
    input_variables=["adjective"],
)

# 一个较短输入的示例，因此选择所有例子。
print(dynamic_prompt.format(adjective="大"))
# -> 给出每个输入的反义词

# -> 输入：快乐
# -> 输出：悲伤

# -> 输入：高
# -> 输出：矮

# -> 输入：充满活力
# -> 输出：倦怠

# -> 输入：大
# -> 输出：

# 一个较长输入的示例，因此只选择一个例子。
long_string = "大和巨大和庞大和宽大和巨大和高大"
print(dynamic_prompt.format(adjective=long_string))
# -> 给出每个输入的反义词

# -> 输入：快乐
# -> 输出：悲伤

# -> 输入：大和巨大和庞大和宽大和巨大和高大
# -> 输出：
