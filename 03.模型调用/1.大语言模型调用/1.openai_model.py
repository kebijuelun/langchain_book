# 导入 OpenAI 模型类
from langchain.llms import OpenAI

# 实例化语言模型
llm = OpenAI(model_name="text-ada-001", max_tokens=128)

# 模型预测
answer = llm("Tell me a joke")
print("answer: {}".format(answer))
# -> answer: Why did the chicken cross the road? To get to the other side!

# 基于 generate 方法的模型预测
texts = ["Tell me a joke", "Tell me a poem"]
llm_result = llm.generate(texts)

# "Tell me a joke" 的模型预测结果
print("Tell me a joke: ", llm_result.generations[0])
# -> Tell me a joke: [Generation(text='\n\nWhy did the chicken cross the road?\n\nTo get to the other side!', generation_info={'finish_reason': 'stop', 'logprobs': None})]

# "Tell me a poem" 的模型预测结果
print("Tell me a poem: ", llm_result.generations[1])
# -> Tell me a poem: [Generation(text="\n\nThe world is a beautiful place,\nThe colors are so bright and true,\nAnd I feel so free and free,\nWhen I'm away from here.\n\nThe sky is so blue,\nAnd the sun is so warm,\nAnd I feel so free and free,\nWhen I'm away from here.", generation_info={'finish_reason': None, 'logprobs': None})]

# Token 数量使用情况统计
print("Token 使用统计: ", llm_result.llm_output)
# -> Token 使用统计: {'token_usage': {'prompt_tokens': 8, 'completion_tokens': 87, 'total_tokens': 95}, 'model_name': 'text-ada-001'}

# Token 预估使用量
print(f'"{texts[0]}" 使用 token 数目为:', llm.get_num_tokens(texts[0]))
# -> "Tell me a joke" 使用 token 数目为: 4
print(f'"{texts[1]}" 使用 token 数目为:', llm.get_num_tokens(texts[1]))
# -> "Tell me a poem" 使用 token 数目为: 4
