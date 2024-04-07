from typing import Dict, List

import numpy as np
from langchain.prompts.example_selector.base import BaseExampleSelector


class CustomExampleSelector(BaseExampleSelector):
    """自定义的样例选择器，继承自BaseExampleSelector类。"""

    def __init__(self, examples: List[Dict[str, str]]):
        """
        初始化CustomExampleSelector类的实例。

        参数:
        - examples (List[Dict[str, str]]): 样例列表，每个样例是一个包含键值对的字典。
        """
        self.examples = examples

    def add_example(self, example: Dict[str, str]) -> None:
        """
        将新的样例添加到存储中的一个键上。

        参数:
        - example (Dict[str, str]): 要添加的样例，是一个包含键值对的字典。
        """
        self.examples.append(example)

    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        """
        根据输入选择要使用的样例。

        参数:
        - input_variables (Dict[str, str]): 输入变量，是一个包含键值对的字典。

        返回:
        - List[dict]: 选择的样例列表，每个样例是一个包含键值对的字典。
        """
        return np.random.choice(self.examples, size=2, replace=False)


examples = [{"foo": "1"}, {"foo": "2"}, {"foo": "3"}]

# 初始化样例选择器。
example_selector = CustomExampleSelector(examples)


# 选择样例
print(example_selector.select_examples({"foo": "foo"}))
# -> [{'foo': '1'} {'foo': '3'}]

# 将新样例添加到样例集中
example_selector.add_example({"foo": "4"})
print(example_selector.examples)
# -> [{'foo': '1'}, {'foo': '2'}, {'foo': '3'}, {'foo': '4'}]

# 选择样例
print(example_selector.select_examples({"foo": "foo"}))
# -> [{'foo': '4'} {'foo': '2'}]
