from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma

# 创建一个 PromptTemplate 对象，用于格式化示例的输入和输出
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="输入：{input}\n输出：{output}",
)

# 创建一组虚构的任务示例，用于创建反义词
examples = [
    {"input": "快乐", "output": "悲伤"},
    {"input": "高", "output": "矮"},
    {"input": "充满活力", "output": "倦怠"},
    {"input": "晴朗", "output": "阴沉"},
    {"input": "有风的", "output": "平静"},
]

# 创建一个 SemanticSimilarityExampleSelector 对象
# 它基于嵌入向量的语义相似度来选择示例
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 可供选择的示例列表
    examples,
    # 用于生成嵌入向量以测量语义相似度的嵌入类
    OpenAIEmbeddings(),
    # 用于存储嵌入向量并进行相似度搜索的 VectorStore 类
    Chroma,
    # 生成示例的数量
    k=1,
)

# 创建一个 FewShotPromptTemplate 对象
# 使用 ExampleSelector 替代示例列表
similar_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="输入：{adjective}\n输出：",
    input_variables=["adjective"],
)

# 输入是一种感觉，所以应该选择快乐/悲伤示例
print(similar_prompt.format(adjective="担忧"))
# -> 给出每个输入的反义词

# -> 输入：充满活力
# -> 输出：倦怠

# -> 输入：担忧
# -> 输出：

# 输入是一种度量，所以应该选择高/矮示例
print(similar_prompt.format(adjective="胖"))
# -> 给出每个输入的反义词

# -> 输入：高
# -> 输出：矮

# -> 输入：胖
# -> 输出：

# 也可以向 SemanticSimilarityExampleSelector 添加新的示例
similar_prompt.example_selector.add_example({"input": "热情", "output": "冷漠"})
