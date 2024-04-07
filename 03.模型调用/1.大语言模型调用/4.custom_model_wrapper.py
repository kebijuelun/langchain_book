from typing import Any, List, Mapping, Optional

from langchain.llms.base import LLM


# 定义CustomLLM，继承LLM类
class CustomLLM(LLM):
    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    # 此处定义的CustomLLM类，实现的功能是，对于输入的prompt文本，输出prompt文本的前n个字符
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[: self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}


# 创建CustomLLM类的实例，得到自定义模型
llm = CustomLLM(n=10)

# 调用自定义模型
print(llm("This is a foobar thing"))
# -> 'This is a '
