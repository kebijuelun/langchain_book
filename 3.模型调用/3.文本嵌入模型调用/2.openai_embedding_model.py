# 导入所需的库
import numpy as np  # 导入numpy库，用于数组操作
from langchain.embeddings import OpenAIEmbeddings  # 导入OpenAIEmbeddings类

# 创建OpenAIEmbeddings实例
embeddings = OpenAIEmbeddings()

# 定义文本
text = "This is a test document."

# 对查询文本进行嵌入
query_result = embeddings.embed_query(text)

# 打印查询结果的形状
print(np.array(query_result).shape)
# -> (1536,)

# 对多个文档进行嵌入
doc_result = embeddings.embed_documents([text, text])

# 打印文档嵌入结果的形状
print(np.array(doc_result).shape)
# -> (2, 1536)

# embed_documents 与 embed_query 的输出结果是一致的
print((np.array(doc_result[0]) == np.array(query_result)).all())
# -> True
