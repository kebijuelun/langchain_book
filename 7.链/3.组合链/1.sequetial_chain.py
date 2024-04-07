from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# 创建一个 LLMChain，根据剧目的中文标题编写剧情简介
llm = OpenAI(temperature=0.7)
template = """你是一位编剧。根据剧目的标题，你的任务是为该剧目编写剧情简介。

剧目标题：{title}
编剧：这是上述剧目的剧情简介："""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)

# 创建一个 LLMChain，根据剧情简介编写剧评
llm = OpenAI(temperature=0.7)
template = """你是一位来自《纽约时报》的戏剧评论家。根据剧情简介，你的任务是为该剧目撰写一篇评论。

剧情简介：
{synopsis}
来自《纽约时报》的戏剧评论家对上述剧目的评论："""
prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_template)

# 创建一个顺序链，按顺序运行上述两个链式调用
from langchain.chains import SimpleSequentialChain

overall_chain = SimpleSequentialChain(
    chains=[synopsis_chain, review_chain], verbose=True
)

review = overall_chain.run("黄昏海滩上的小女孩和大黄狗")
# -> > Entering new  chain...
# -> 在一个美丽的夏天，一个小女孩和一只可爱的大黄狗走进了一片黄昏海滩。他们开始了一段有趣而又充满感情的旅程，穿过花园，穿越森林，游览湖泊，最终到达海滩。在海滩上，小女孩和大黄狗发现了他们的真正的友谊，他们一起度过了一个难忘的夏天。最后，他们回到
# -> 《夏天的海滩》是一部充满温情的剧目，让观众感受到了最真实的友谊。它以一种新颖而又有趣的方式呈现了小女孩和大黄狗的旅程，他们穿过花园，穿越森林，游览湖泊，最终到达了海滩，探索出他们的真正的友谊。这部剧目的演员们出色地表现出了他们的角色
# -> > Finished chain.

print(review)
# 《夏天的海滩》是一部充满温情的剧目，让观众感受到了最真实的友谊。它以一种新颖而又有趣的方式呈现了小女孩和大黄狗的旅程，他们穿过花园，穿越森林，游览湖泊，最终到达了海滩，探索出他们的真正的友谊。这部剧目的演员们出色地表现出了他们的角色
