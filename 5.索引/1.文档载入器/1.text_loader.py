# 导入所需的文档加载器模块
from langchain.document_loaders import TextLoader

# 创建一个文本加载器实例，并指定要加载的文档路径为"./text.txt"
loader = TextLoader("./test.txt")

# 调用加载器的load方法，加载指定路径下的文档
print(loader.load())
# -> [Document(page_content='document loader\nexample\ntest\n', metadata={'source': './test.txt'})]
