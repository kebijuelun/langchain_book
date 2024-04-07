from typing import Any, Dict, List

import spacy
from langchain import ConversationChain, OpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.schema import BaseMemory
from pydantic import BaseModel

# 加载英文 spacy 模型（注意需要在终端运行以下命令，安装 spacy 库并下载 en_core_web_lg 文件）
# pip install spacy
# python -m spacy download en_core_web_lg
nlp = spacy.load("en_core_web_lg")


class SpacyEntityMemory(BaseMemory, BaseModel):
    """用于存储实体信息的记忆类。"""

    # 定义字典以存储实体信息。
    entities: dict = {}
    # 定义用于将实体信息传递到提示中的键。
    memory_key: str = "entities"

    def clear(self):
        self.entities = {}

    @property
    def memory_variables(self) -> List[str]:
        """定义要提供给提示的变量。"""
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """加载记忆变量，此处为实体键。"""
        # 获取输入文本并运行通过 spacy 处理。
        doc = nlp(inputs[list(inputs.keys())[0]])
        # 提取已知实体的信息，如果存在的话。
        entities = [
            self.entities[str(ent)] for ent in doc.ents if str(ent) in self.entities
        ]
        # 返回组合的实体信息以放入上下文中。
        return {self.memory_key: "\n".join(entities)}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """将此对话的上下文保存到缓冲区中。"""
        # 获取输入文本并运行通过 spacy 处理。
        text = inputs[list(inputs.keys())[0]]
        doc = nlp(text)
        # 对于提到的每个实体，将此信息保存到字典中。
        for ent in doc.ents:
            ent_str = str(ent)
            if ent_str in self.entities:
                self.entities[ent_str] += f"\n{text}"
            else:
                self.entities[ent_str] = text


# 定义提示模板，用于人与 AI 之间的对话
template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. You are provided with information about entities the Human mentions, if relevant.

Relevant entity information:
{entities}

Conversation:
Human: {input}
AI:"""
prompt = PromptTemplate(input_variables=["entities", "input"], template=template)

# 创建 OpenAI 实例
llm = OpenAI(temperature=0)
# 创建 ConversationChain 实例，包括自定义记忆
conversation = ConversationChain(
    llm=llm, prompt=prompt, verbose=True, memory=SpacyEntityMemory()
)

# 针对第一个示例进行预测，其中没有关于小明的先前知识
print(conversation.predict(input="Harrison likes machine learning"))
# -> > Entering new ConversationChain chain...
# -> Prompt after formatting:
# -> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. You are provided with information about entities the Human mentions, if relevant.

# -> Relevant entity information:


# -> Conversation:
# -> Human: Harrison likes machine learning
# -> AI:

# -> > Finished chain.
# -> That's great to hear! Machine learning is a fascinating field of study. It involves using algorithms to analyze data and make predictions. Have you ever studied machine learning, Harrison?


# 针对第二个示例进行预测，这次我们可以看到它提取了与小明有关的信息
print(
    conversation.predict(
        input="What do you think Harrison's favorite subject in college was?"
    )
)
# -> > Entering new ConversationChain chain...
# -> Prompt after formatting:
# -> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. You are provided with information about entities the Human mentions, if relevant.

# -> Relevant entity information:
# -> Harrison likes machine learning

# -> Conversation:
# -> Human: What do you think Harrison's favorite subject in college was?
# -> AI:

# -> > Finished chain.
# ->  From what I know about Harrison, I believe his favorite subject in college was machine learning. He has expressed a strong interest in the subject and has mentioned it often.
