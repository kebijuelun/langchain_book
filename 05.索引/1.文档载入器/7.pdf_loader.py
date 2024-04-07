导入PyPDFLoader类
from langchain.document_loaders import PyPDFLoader

# 创建PyPDFLoader对象，并指定PDF文件路径
loader = PyPDFLoader("./layout-parser-paper.pdf")

# 使用loader的load_and_split()方法加载并拆分PDF文档的页面
pages = loader.load_and_split()

# 打印第一页的内容
print(pages[0])
# page_content='LayoutParser : A Uni\x0ced Toolkit for Deep\nLearning Based Document ...... Jun 2021' metadata={'source': './layout-parser-paper.pdf', 'page': 0}
