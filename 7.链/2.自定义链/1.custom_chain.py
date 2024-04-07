from __future__ import annotations

from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import (
    AsyncCallbackManagerForChainRun,
    CallbackManagerForChainRun,
)
from langchain.chains.base import Chain
from langchain.prompts.base import BasePromptTemplate
from pydantic import Extra


class MyCustomChain(Chain):
    """
    自定义链的示例。
    """

    prompt: BasePromptTemplate
    """要使用的Prompt对象。"""
    llm: BaseLanguageModel
    output_key: str = "text"  #: :meta private:

    class Config:
        """此pydantic对象的配置。"""

        extra = Extra.forbid
        arbitrary_types_allowed = True

    @property
    def input_keys(self) -> List[str]:
        """返回Prompt所期望的输入键列表。

        :meta private:
        """
        return self.prompt.input_variables

    @property
    def output_keys(self) -> List[str]:
        """总是返回text键。

        :meta private:
        """
        return [self.output_key]

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        """
        同步执行自定义链。

        :param inputs: 输入值的字典。
        :param run_manager: 用于跟踪执行的回调管理器。
        :return: 包含输出键和生成的文本的字典。
        """
        # 自定义链的逻辑在这里
        # 这只是一个模仿LLMChain的示例
        prompt_value = self.prompt.format_prompt(**inputs)

        # 每当调用语言模型或另一个链时，应传递回调管理器。
        # 这允许内部运行由外部运行注册的任何回调跟踪。
        # 您始终可以通过调用`run_manager.get_child()`来获取此的回调管理器，如下所示。
        response = self.llm.generate_prompt(
            [prompt_value], callbacks=run_manager.get_child() if run_manager else None
        )

        # 如果要记录关于此运行的信息，可以通过调用`run_manager`上的方法来实现，如下所示。
        # 这将触发为该事件注册的任何回调。
        if run_manager:
            run_manager.on_text("记录此运行的一些内容")

        return {self.output_key: response.generations[0][0].text}

    async def _acall(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        """
        异步执行自定义链。

        :param inputs: 输入值的字典。
        :param run_manager: 用于跟踪执行的回调管理器。
        :return: 包含输出键和生成的文本的字典。
        """
        # 自定义链的逻辑在这里
        # 这只是一个模仿LLMChain的示例
        prompt_value = self.prompt.format_prompt(**inputs)

        # 每当调用语言模型或另一个链时，应传递回调管理器。
        # 这允许内部运行由外部运行注册的任何回调跟踪。
        # 您始终可以通过调用`run_manager.get_child()`来获取此的回调管理器，如下所示。
        response = await self.llm.agenerate_prompt(
            [prompt_value], callbacks=run_manager.get_child() if run_manager else None
        )

        # 如果要记录关于此运行的信息，可以通过调用`run_manager`上的方法来实现，如下所示。
        # 这将触发为该事件注册的任何回调。
        if run_manager:
            await run_manager.on_text("记录此运行的一些内容")

        return {self.output_key: response.generations[0][0].text}

    @property
    def _chain_type(self) -> str:
        return "my_custom_chain"


from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate

chain = MyCustomChain(
    prompt=PromptTemplate.from_template("告诉我们一个关于{topic}的笑话"),
    llm=ChatOpenAI(),
)

result = chain.run({"topic": "美国"}, callbacks=[StdOutCallbackHandler()])
print(result)
# -> > Entering new  chain...
# -> 记录此运行的一些内容
# -> > Finished chain.
# -> 有一天，一个美国人、一个英国人和一个中国人在讨论他们国家的文化。美国人说：“我们国家的文化是最先进的，我们有好莱坞、摇滚乐和自由。”英国人说：“我们国家的文化是最悠久的，我们有莎士比亚、文学和皇室。”中国人说：“我们
# -> 国家的文化是最深厚的，我们有5000年的历史和文化传统。”
# -> 这时，一个墨西哥人走过来，听到了他们的谈话，很不屑地说：“那又怎样？我们有塔科贝拉！”其他人都不明白，问他：“什么是塔科贝拉？”墨西哥人得意地说：“那是我们国家最有名的一种美食，用玉米面制成的薄饼，非常好吃！”
# -> 大家都笑了，美国人说：“那不算什么，我们有汉堡包！”英国人说：“那也不算什么，我们有鱼和薯条！”中国人想了想，然后说：“那我告诉你们一个最厉害的东西，我们有糯米团！”
# -> 其他人不解地问：“什么是糯米团？”中国人笑着说：“那是我们国家最有名的一种美食，用糯米制成的球形食品，非常好吃！”
# -> 大家都笑了，墨西哥人摇摇头：“你们还是不懂，塔科贝拉是一种生活方式！”
