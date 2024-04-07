# 导入所需模块
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationSummaryMemory

# 创建一个 ConversationSummaryMemory 实例，使用 OpenAI 语言模型，并设置返回消息
memory = ConversationSummaryMemory(llm=OpenAI(temperature=0), return_messages=True)

# 将包含用户输入和 AI 回应的上下文保存到内存中
memory.save_context(
    {
        "input": "Hello, today I want to go boating in Beihai Park with Little Red. She's my good friend, and she has an adorable little dog named Mantou."
    },
    {
        "output": "Hello! Beihai Park is a great choice, and boating is a wonderful activity. I hope you and Little Red have a pleasant time. Mantou must be an adorable little dog. Have a great time!"
    },
)

# 载入内存变量
memory.load_memory_variables({})

# 获取内存中的聊天消息
messages = memory.chat_memory.messages

# 设置一个空的前一摘要
previous_summary = ""

# 预测基于消息和前一摘要的新摘要
memory.predict_new_summary(messages, previous_summary)
# -> The human asked the AI to go to Beihai Park with their friend, Little Red, and her pet dog, Mantou. The AI responded positively, wishing them a pleasant time and expressing admiration for Mantou.

# 创建一个 OpenAI 语言模型实例
llm = OpenAI(temperature=0)

# 创建一个 ConversationChain 实例，结合语言模型、内存和启用详细模式
conversation_with_summary = ConversationChain(llm=llm, memory=memory, verbose=True)

# 对话机器人对新输入的回应
conversation_with_summary.predict(
    input="Do you remember who I wanted to go boating with at Beihai Park today?"
)
# -> Yes, I remember that you wanted to go boating with your friend, Little Red, and her pet dog, Mantou. I think it will be a great time and I'm sure Mantou will enjoy it too!
