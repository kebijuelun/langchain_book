# 打开文件并读取内容
with open("./state_of_the_union.txt") as f:
    state_of_the_union = f.read()

# 导入文本分割器模块
from langchain.text_splitter import CharacterTextSplitter

# 创建文本分割器对象
text_splitter = CharacterTextSplitter(
    separator="\n\n",  # 文本分割符为两个换行符
    chunk_size=1000,  # 分割后的文本块大小为1000个字符
    chunk_overlap=200,  # 分割文本块之间的重叠部分为200个字符
    length_function=len,  # 计算文本长度的函数为len
)

# 使用文本分割器将文本分割为多个文档
texts = text_splitter.create_documents([state_of_the_union])

# 打印第一个文档
print(texts[0])
