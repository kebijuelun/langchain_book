# 导入所需的目录加载器模块
from langchain.document_loaders import DirectoryLoader

# 创建一个目录加载器实例，并指定要加载的目录路径为'./'，并使用通配符筛选要加载的文件类型为'**/*.txt'
loader = DirectoryLoader("./", glob="**/*.txt")

# 调用加载器的load方法，从指定目录加载所有符合条件的文档
docs = loader.load()

print(len(docs))
print(docs)
# -> 1
# -> [Document(page_content='document loader\n\nexample\n\ntest', metadata={'source': 'test.txt'})]
