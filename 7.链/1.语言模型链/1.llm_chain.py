from langchain import LLMChain, OpenAI, PromptTemplate

# 创建一个提示模板，用于生成公司名称
prompt_template = "What is a good name for a company that makes {product}?"

# 创建一个OpenAI语言模型实例
llm = OpenAI(temperature=0)

# 创建一个LLMChain，将语言模型和提示模板传递进去
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))

# 使用llm_chain进行单次调用，传入产品名称"colorful socks"
print(llm_chain("colorful socks"))
# -> {'product': 'colorful socks', 'text': '\n\nSocktastic!'}

# 准备一个输入列表
input_list = [{"product": "socks"}, {"product": "computer"}, {"product": "shoes"}]

# 使用llm_chain对输入列表进行批量调用
print(llm_chain.apply(input_list))
# -> [{'text': '\n\nSocktastic!'}, {'text': '\n\nTechCore Solutions.'}, {'text': '\n\nFootwear Factory.'}]

# 使用llm_chain对输入列表进行生成文本
print(llm_chain.generate(input_list))
# generations=[[Generation(text='\n\nCozy Toes Socks.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='\n\nTechCore Solutions.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='\n\nFootwear Factory.', generation_info={'finish_reason': 'stop', 'logprobs': None})]] llm_output={'token_usage': {'prompt_tokens': 36, 'completion_tokens': 21, 'total_tokens': 57}, 'model_name': 'text-davinci-003'}

# 导入输出解析器CommaSeparatedListOutputParser
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()

# 创建一个模板，用于列出彩虹中的颜色
template = """List all the colors in a rainbow"""
# 创建一个PromptTemplate，使用刚才创建的模板和输出解析器
prompt = PromptTemplate(
    template=template, input_variables=[], output_parser=output_parser
)

# 创建一个新的LLMChain，使用新的PromptTemplate和之前创建的语言模型实例
llm_chain = LLMChain(prompt=prompt, llm=llm)

# 使用llm_chain进行预测，并打印结果
print(llm_chain.predict())
# -> Red, orange, yellow, green, blue, indigo, violet

# 使用llm_chain进行预测并解析结果
print(llm_chain.predict_and_parse())
# -> ['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
