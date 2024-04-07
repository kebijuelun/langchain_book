from langchain import PromptTemplate

## Create a prompt template
# 一个没有输入变量的示例提示词
no_input_prompt = PromptTemplate(input_variables=[], template="给我讲一个笑话。")
print(no_input_prompt.format())
# -> "给我讲一个笑话。"

# 一个带有一个输入变量的示例提示词
one_input_prompt = PromptTemplate(
    input_variables=["adjective"], template="给我讲一个{adjective}的笑话。"
)
print(one_input_prompt.format(adjective="好笑的"))
# -> "给我讲一个好笑的笑话。"

# 一个带有多个输入变量的示例提示词
multiple_input_prompt = PromptTemplate(
    input_variables=["adjective", "content"], template="给我讲一个关于{content}的{adjective}笑话。"
)
print(multiple_input_prompt.format(adjective="好笑的", content="猪"))
# -> "给我讲一个关于猪的好笑的笑话。"

## Template formats
# with f-string
template = "告诉我一个{adjective}的笑话，关于{content}的。"

prompt_template = PromptTemplate.from_template(template)
prompt_template.input_variables
# -> ['adjective', 'content']
print(prompt_template.format(adjective="有趣的", content="猪"))
# -> 告诉我一个有趣的笑话，关于猪的。

# with jinja2 (在运行之前，请确保已安装 jinja2)
jinja2_template = "告诉我一个{{ adjective }}的笑话，关于{{ content }}的"
prompt_template = PromptTemplate.from_template(
    template=jinja2_template, template_format="jinja2"
)

print(prompt_template.format(adjective="有趣的", content="猪"))
# -> 告诉我一个有趣的笑话，关于猪的。
