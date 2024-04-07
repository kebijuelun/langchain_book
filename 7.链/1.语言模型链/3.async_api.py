import asyncio
import time

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


def generate_serially():
    """
    串行生成文本的函数。
    """
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for _ in range(5):
        resp = chain.run(product="toothpaste")
        print(resp)


async def async_generate(chain):
    """
    异步生成文本的函数。

    :param chain: LLMChain对象。
    """
    resp = await chain.arun(product="toothpaste")
    print(resp)


async def generate_concurrently():
    """
    并发生成文本的函数。
    """
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    tasks = [async_generate(chain) for _ in range(5)]
    await asyncio.gather(*tasks)


s = time.perf_counter()
asyncio.run(generate_concurrently())
elapsed = time.perf_counter() - s
print("\033[1m" + f"并发执行时间为{elapsed:0.2f}秒。" + "\033[0m")
# -> BrightSmile Toothpaste Company
# -> BrightSmile Toothpaste Co.
# -> BrightSmile Toothpaste
# -> Gleaming Smile Inc.
# -> SparkleSmile Toothpaste
# -> 并发执行时间为1.54秒

s = time.perf_counter()
generate_serially()
elapsed = time.perf_counter() - s
print("\033[1m" + f"串行执行时间为{elapsed:0.2f}秒。" + "\033[0m")
# -> BrightSmile Toothpaste Co.
# -> MintyFresh Toothpaste Co.
# -> SparkleSmile Toothpaste.
# -> Pearly Whites Toothpaste Co.
# -> BrightSmile Toothpaste.
# -> 串行执行时间为1.54秒
