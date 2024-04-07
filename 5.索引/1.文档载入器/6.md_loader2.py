# 导入所需的MarkDown加载器模块
from langchain.document_loaders import UnstructuredMarkdownLoader

# 定义Markdown文件路径
markdown_path = "./notebook.md"

# 创建UnstructuredMarkdownLoader对象，并指定Markdown文件路径
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")

# 使用loader加载Markdown文档，返回加载后的数据
data = loader.load()

# 打印加载后的数据
print(data)
# -> [Document(page_content='Notebook', metadata={'source': './notebook.md', 'filename': 'notebook.md', 'file_directory': '.', 'filetype': 'text/markdown', 'page_number': 1, 'category': 'Title'}),
# -> Document(page_content='This notebook covers how to load data from an .ipynb notebook into a format suitable by LangChain.', metadata={'source': './notebook.md', 'filename': 'notebook.md', 'file_directory': '.', 'filetype': 'text/markdown', 'page_number': 1, 'category': 'NarrativeText'}),
# -> ......
# -> Document(page_content='python\nloader.load(include_outputs=True, max_output_length=20, remove_newline=True)', metadata={'source': './notebook.md', 'filename': 'notebook.md', 'file_directory': '.', 'filetype': 'text/markdown', 'page_number': 1, 'category': 'Title'})]
