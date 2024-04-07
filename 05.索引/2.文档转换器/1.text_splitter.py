# 读取文件'./state_of_the_union.txt'的内容
with open("./state_of_the_union.txt") as f:
    state_of_the_union = f.read()

# 导入RecursiveCharacterTextSplitter类
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 创建一个文本转环器实例
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    add_start_index=True,
)

# 使用文本拆分器拆分“state_of_the_union”文本
texts = text_splitter.create_documents([state_of_the_union])

# 打印拆分后的文本
print(texts[0])
print(texts[1])
# -> page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and' metadata={'start_index': 0}
# -> page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.' metadata={'start_index': 82}
