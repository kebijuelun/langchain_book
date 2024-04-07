import matplotlib.pyplot as plt
import numpy as np
import openai
import pandas as pd
from sklearn.manifold import TSNE


# 定义获取文本嵌入的函数
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]


# 定义输入数据
table_data = [
    {"text": "big dog", "label": 0},
    {"text": "strong dog", "label": 0},
    {"text": "large dog", "label": 0},
    {"text": "little cat", "label": 1},
    {"text": "small cat", "label": 1},
    {"text": "kitten", "label": 1},
]
df = pd.DataFrame(table_data, columns=["text", "label"])

# 打印原始输入数据
print("> raw input data:\n", df)
# ->         text  label
# -> 0     big dog      0
# -> 1  strong dog      0
# -> 2   large dog      0
# -> 3  little cat      1
# -> 4   small cat      1
# -> 5      kitten      1

# 对每个文本进行文本嵌入
df["ada_embedding"] = df.text.apply(
    lambda x: get_embedding(x, model="text-embedding-ada-002")
)

# 打印进行文本嵌入后的数据
print("> after text embedding:\n", df)
# ->           text  label                                      ada_embedding
# -> 0     big dog      0  [-0.012279368937015533, -0.017828509211540222,...
# -> 1  strong dog      0  [-0.021650593727827072, -0.01337242592126131, ...
# -> 2   large dog      0  [-0.005486527923494577, -0.014770413748919964,...
# -> 3  little cat      1  [-0.023309631273150444, 0.006952110677957535, ...
# -> 4   small cat      1  [-0.01614973694086075, 0.00723886676132679, 0....
# -> 5      kitten      1  [-0.023020850494503975, -0.0031561367213726044...

# 使用 t-SNE 进行降维
tsne = TSNE(
    n_components=2, perplexity=2, random_state=42, init="random", learning_rate=200
)

matrix = df.ada_embedding.to_list()
vis_dims = tsne.fit_transform(np.array(matrix))

x = [x for x, _ in vis_dims]
y = [y for _, y in vis_dims]
labels = df.label.to_list()

# 根据标签绘制散点图
for i in range(len(x)):
    if labels[i] == 0:
        s1 = plt.scatter(x[i], y[i], c="darkorange", alpha=0.8, linewidths=6)
    elif labels[i] == 1:
        s2 = plt.scatter(x[i], y[i], c="darkgreen", alpha=0.8, linewidths=6, marker="^")

# 设置图表标题和图例
plt.title("Text embedding visualized using t-SNE")
plt.legend((s1, s2), ("dog", "cat"), loc="best")

# 显示图表
plt.show()
