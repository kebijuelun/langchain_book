from langchain.llms import OpenAI  # 导入语言模型类
from langchain.output_parsers import PydanticOutputParser  # 导入输出解析器类
from langchain.prompts import PromptTemplate  # 导入提示模板类
from pydantic import BaseModel, Field, validator  # 导入基本模型类、字段类和验证器类

model_name = "text-davinci-003"  # 设置语言模型的名称
temperature = 0.0  # 设置温度参数
model = OpenAI(model_name=model_name, temperature=temperature)  # 初始化语言模型对象


# 定义所需的数据结构
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")  # 用于设置笑话问题的字段
    punchline: str = Field(description="answer to resolve the joke")  # 用于解答笑话的字段

    # 使用 Pydantic 可以轻松添加自定义验证逻辑
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")  # 如果问题不以问号结尾，则抛出异常
        return field


# 设置解析器，并将格式说明注入到提示模板中
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 发出查询以提示语言模型填充数据结构
joke_query = "Tell me a joke."  # 笑话查询字符串
_input = prompt.format_prompt(query=joke_query)  # 格式化提示模板，生成输入对象
print(_input.to_string())
"""
Answer the user query.
The output should be formatted as a JSON instance that conforms to the JSON schema below.

As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}}
the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.

Here is the output schema:
```
{"properties": {"setup": {"title": "Setup", "description": "question to set up a joke", "type": "string"}, "punchline": {"title": "Punchline", "description": "answer to resolve the joke", "type": "string"}}, "required": ["setup", "punchline"]}
```
Tell me a joke.
"""

output = model(_input.to_string())  # 调用语言模型，传入输入对象，获取输出结果
print(output)
# -> {"setup": "Why did the chicken cross the road?", "punchline": "To get to the other side!"}

print(parser.parse(output))
# -> setup='Why did the chicken cross the road?' punchline='To get to the other side!'
from IPython import embed

embed()
