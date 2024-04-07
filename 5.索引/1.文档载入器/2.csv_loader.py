# 导入所需的CSV加载器模块
from langchain.document_loaders.csv_loader import CSVLoader

# 创建一个CSV加载器实例，并指定要加载的文件路径为'./test_nominal.csv'
# loader = CSVLoader(file_path='/home/lwz/zwp_code/langchain-master/tests/unit_tests/document_loaders/test_docs/csv/test_nominal.csv')
loader = CSVLoader(file_path="./test_nominal.csv")

# 调用加载器的load方法，加载CSV文件中的数据
data = loader.load()

print(data)
# -> [Document(page_content='column1: value1\ncolumn2: value2\ncolumn3: value3', metadata={'source': './test_nominal.csv', 'row': 0}),
# -> Document(page_content='column1: value4\ncolumn2: value5\ncolumn3: value6', metadata={'source': './test_nominal.csv', 'row': 1})]
