# 导入所需的MarkDown加载器模块
from langchain.document_loaders import UnstructuredMarkdownLoader

# 定义Markdown文件路径
markdown_path = "./notebook.md"

# 创建UnstructuredMarkdownLoader对象，并指定Markdown文件路径
loader = UnstructuredMarkdownLoader(markdown_path)

# 使用loader加载Markdown文档，返回加载后的数据
data = loader.load()

# 打印加载后的数据
print(data)
# -> [Document(page_content='Notebook\n\nThis notebook covers how to load data from an .ipynb notebook into a format suitable by LangChain.\n\npython\nfrom langchain.document_loaders import NotebookLoader\n\npython\nloader = NotebookLoader("example_data/notebook.ipynb")\n\nNotebookLoader.load() loads the .ipynb notebook file into a Document object.\n\nParameters:\n\ninclude_outputs (bool): whether to include cell outputs in the resulting document (default is False).\n\nmax_output_length (int): the maximum number of characters to include from each cell output (default is 10).\n\nremove_newline (bool): whether to remove newline characters from the cell sources and outputs (default is False).\n\ntraceback (bool): whether to include full traceback (default is False).\n\npython\nloader.load(include_outputs=True, max_output_length=20, remove_newline=True)', metadata={'source': './notebook.md'})]
