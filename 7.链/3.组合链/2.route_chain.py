from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# 定义物理学问题的模板
physics_template = """你是一位非常聪明的物理学教授。你擅长以简明易懂的方式回答物理学问题。当你不知道答案时，你会坦诚承认。

以下是一个问题：
{input}"""

# 定义数学问题的模板
math_template = """你是一位很棒的数学家。你擅长回答数学问题。你之所以这么好，是因为你能够将复杂的问题分解成各个组成部分，回答这些组成部分，然后将它们整合在一起回答更广泛的问题。

以下是一个问题：
{input}"""

# 定义不同类型的提示信息
prompt_infos = [
    {
        "name": "physics",
        "description": "适用于回答物理学问题",
        "prompt_template": physics_template,
    },
    {
        "name": "math",
        "description": "适用于回答数学问题",
        "prompt_template": math_template,
    },
]

llm = OpenAI()

destination_chains = {}
# 根据提示信息创建目标链
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

# 创建默认链
default_chain = ConversationChain(llm=llm, output_key="text")

from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

# 创建路由器的模板
destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)

# 创建路由器链
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

# 创建多提示链
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

# 运行链以回答关于黑体辐射的问题
print(chain.run("什么是黑体辐射？"))
# -> physics: {'input': '什么是黑体辐射？'}
# -> 黑体辐射是指物体受到环境温度的影响而发射出来的一种光谱。它是由物体自身的温度控制，当它的温度上升时，它会发出越来越多的热量，从而发出越来越多的光谱。当物体受到高温影响时，它会发出越来越多的热量，从而发出越来越多的黑体辐射。

# 运行链以回答一个问题：大于40的第一个质数加上1可以被3整除的是什么数？
print(chain.run("大于40的第一个质数加上1可以被3整除的是什么数？"))
# -> math: {'input': 'What is the first prime number greater than 40 that is divisible by 3 when 1 is added to it?'}
# -> 答案：43。因为40加1后是41，是一个质数，但不是3的倍数，而42加1后是43，既是质数又是3的倍数，所以43就是第一个满足条件的质数。

# 运行链以回答关于云的类型的问题
print(chain.run("什么是那种云的名字？"))
# -> None: {'input': '什么是那种云的名字？'}
# -> 你是指某个特定的云类型吗？

# 对路由链模板可视化
from pprint import pprint

pprint(router_template)
# ('Given a raw text input to a language model select the model prompt best '
#  'suited for the input. You will be given the names of the available prompts '
#  'and a description of what the prompt is best suited for. You may also revise '
#  'the original input if you think that revising it will ultimately lead to a '
#  'better response from the language model.\n'
#  '\n'
#  '<< FORMATTING >>\n'
#  'Return a markdown code snippet with a JSON object formatted to look like:\n'
#  '```json\n'
#  '{{\n'
#  '    "destination": string \\ name of the prompt to use or "DEFAULT"\n'
#  '    "next_inputs": string \\ a potentially modified version of the original '
#  'input\n'
#  '}}\n'
#  '```\n'
#  '\n'
#  'REMEMBER: "destination" MUST be one of the candidate prompt names specified '
#  'below OR it can be "DEFAULT" if the input is not well suited for any of the '
#  'candidate prompts.\n'
#  'REMEMBER: "next_inputs" can just be the original input if you don\'t think '
#  'any modifications are needed.\n'
#  '\n'
#  '<< CANDIDATE PROMPTS >>\n'
#  'physics: 适用于回答物理学问题\n'
#  'math: 适用于回答数学问题\n'
#  '\n'
#  '<< INPUT >>\n'
#  '{input}\n'
#  '\n'
#  '<< OUTPUT >>\n')
