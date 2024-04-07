from langchain import FewShotPromptTemplate, PromptTemplate

# 首先，创建少样本示例的列表。
examples = [
    {"word": "快乐", "antonym": "悲伤"},
    {"word": "高", "antonym": "矮"},
]

# 接下来，我们指定用于格式化提供的示例的模板。
# 我们使用 `PromptTemplate` 类来实现这一点。
example_formatter_template = """单词：{word}
反义词：{antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

# 最后，我们创建 `FewShotPromptTemplate` 对象。
few_shot_prompt = FewShotPromptTemplate(
    # 这些是我们要插入到提示中的示例。
    examples=examples,
    # 这是当我们将示例插入到提示中时，我们想要格式化示例的方式。
    example_prompt=example_prompt,
    # 前缀是一些文本，位于提示中的示例之前。
    # 通常，这包括一些说明。
    prefix="给出每个输入的反义词\n",
    # 后缀是一些文本，位于提示中的示例之后。
    # 通常，这是用户输入的位置。
    suffix="单词：{input}\n反义词：",
    # 输入变量是整体提示所期望的变量。
    input_variables=["input"],
    # 示例分隔符是我们将前缀、示例和后缀连接在一起的字符串。
    example_separator="\n",
)

# 现在我们可以使用 `format` 方法生成一个提示。
print(few_shot_prompt.format(input="大"))
# -> 给出每个输入的反义词
# ->
# -> 单词：快乐
# -> 反义词：悲伤
# ->
# -> 单词：高
# -> 反义词：矮
# ->
# -> 单词：大
# -> 反义词：
from IPython import embed

embed()
