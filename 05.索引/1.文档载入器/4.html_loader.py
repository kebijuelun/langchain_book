# 导入所需的HTML加载器模块
from langchain.document_loaders import UnstructuredHTMLLoader

# 定义要加载的 HTML 文件路径
# html_file = "example_data/fake-content.html"
html_file = "/home/lwz/zwp_code/langchain-master/docs/extras/modules/data_connection/document_loaders/integrations/example_data/fake-content.html"
# 文件内容如下：
# <!DOCTYPE html>
# <html>
# <head><title>Test Title</title>
# </head>
# <body>

# <h1>My First Heading</h1>
# <p>My first paragraph.</p>

# </body>
# </html>

# 创建一个 UnstructuredHTMLLoader 实例，并将 HTML 文件路径作为参数传递给构造函数
loader = UnstructuredHTMLLoader(html_file)

# 调用加载器的 load 方法加载 HTML 文件并返回结果
data = loader.load()

# 打印加载的数据
print(data)
# -> [Document(page_content='My First Heading\n\nMy first paragraph.', metadata={'source': 'example_data/fake-content.html'})]
