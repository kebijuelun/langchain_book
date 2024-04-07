from pprint import pprint

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

# 创建一个ChatOpenAI对象作为LLM（Large Language Model）聊天模型的实例
llm = ChatOpenAI()

# 创建一个聊天提示模板，定义了模型与用户之间的交互
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "你是一个友好的聊天机器人，正在与人进行对话，你会遵循人的所有指令，如果人让你扮演某个角色，你会一直扮演该角色直到人说可以停止扮演。"
        ),
        # 此处的 `variable_name` 必须与记忆(memory)中的名称对应
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# 注意我们设置 `return_messages=True`，以适应MessagesPlaceholder
# 注意 `"chat_history"` 与MessagesPlaceholder的名称对齐
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 创建一个LLMChain，整合了LLM、提示模板和记忆
conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

# 调用LLMChain并传递问题变量 - `chat_history` 将由记忆(memory)填充
response = conversation({"question": "我的偶像是篮球运动员科比布莱恩特，你现在需要假扮成科比和我聊天"})
print(response["text"])
# -> 当然没问题！你好，我是科比布莱恩特。很高兴能和你聊天！请问有什么关于篮球或者其他事情我可以帮助你的吗？

response = conversation({"question": "如何提升我的投篮准确度？"})
print(response["text"])
# -> 嗨！要提高投篮准确度，有几个关键点你可以注意一下：

# -> 1. 基本功：确保你的投篮姿势正确。双脚分开与肩同宽，身体略微弯曲，手臂握球放松。重要的是要有稳定的平衡和统一的动作。

# -> 2. 眼睛注视目标：在投篮的时候，要专注于篮筐或者篮板。不要把目光转移到球或者自己的手上，集中注意力于目标，这样可以提高准确度。

# -> 3. 练习：投篮是需要不断练习的。找到一个合适的练习时间和地点，每天坚持练习投篮动作和技巧。可以从近距离开始，逐渐增加距离和难度，提高准确度和稳定性。

# -> 4. 视频分析：录像自己的投篮动作，然后仔细观察和分析。看看是否存在一些不规范的动作或者技巧，然后进行调整和改进。

# -> 5. 心理调节：保持积极的心态和自信心，相信自己可以做到。不要过分焦虑或者紧张，放松心情，享受投篮的过程。

# -> 希望这些提示能对你有所帮助！记住，不断的练习和坚持是提高投篮准确度的关键。

response = conversation({"question": "凌晨4点的洛杉矶是什么样的？"})
print(response["text"])
# -> 凌晨4点的洛杉矶通常是相当安静的。大部分人都在这个时候休息睡觉，所以街上的车辆和行人都会相对较少。夜晚的洛杉矶有时会有一些噪音和活动，但在凌晨4点，城市会更加宁静。你可以看到一些早起的晨运者或者清洁工人在街上工作，但整体来说，城市还是相当宁静的。如果你在那个时候外出，你可能会感受到一种独特的宁静和寂静的氛围。

pprint(response["chat_history"])
# -> [HumanMessage(content='我的偶像是篮球运动员科比布莱恩特，你现在需要假扮成科比和我聊天', additional_kwargs={}, example=False),
# -> AIMessage(content='当然没问题！你好，我是科比布莱恩特。很高兴能和你聊天！请问有什么关于篮球或者其他事情我可以帮助你的吗？', additional_kwargs={}, example=False),
# -> HumanMessage(content='如何提升我的投篮准确度？', additional_kwargs={}, example=False),
# -> AIMessage(content='嗨！要提高投篮准确度，有几个关键点你可以注意一下：\n\n1. 基本功：确保你的投篮姿势正确。双脚分开与肩同宽，身体略微弯曲，手臂握球放松。重要的是要有稳定的平衡和统一的动作。\n\n2. 眼睛注视目标：在投篮的时候，要专注于篮筐或者篮板。不要把目光转移到球或者自己的手上，集中注意力于目标，这样可以提高准确度。\n\n3. 练习：投篮是需要不断练习的。找到一个合适的练习时间和地点，每天坚持练习投篮动作和技巧。可以从近距离开始，逐渐增加距离和难度，提高准确度和稳定性。\n\n4. 视频分析：录像自己的投篮动作，然后仔细观察和分析。看看是否存在一些不规范的动作或者技巧，然后进行调整和改进。\n\n5. 心理调节：保持积极的心态和自信心，相信自己可以做到。不要过分焦虑或者紧张，放松心情，享受投篮的过程。\n\n希望这些提示能对你有所帮助！记住，不断的练习和坚持是提高投篮准确度的关键。加油！', additional_kwargs={}, example=False),
# -> HumanMessage(content='凌晨4点的洛杉矶是什么样的？', additional_kwargs={}, example=False),
# -> AIMessage(content='凌晨4点的洛杉矶通常是相当安静的。大部分人都在这个时候休息睡觉，所以街上的车辆和行人都会相对较少。夜晚的洛杉矶有时会有一些噪音和活动，但在凌晨4点，城市会更加宁静。你可以看到一些早起的晨运者或者清洁工人在街上工作，但整体来说，城市还是相当宁静的。如果你在那个时候外出，你可能会感受到一种独特的宁静和寂静的氛围。', additional_kwargs={}, example=False)]
