import os

from langchain import HuggingFaceHub

# 设置 Hugging Face Hub 的 API Token（请替换为您自己的 API Token）
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_xxx"

# 指定要使用的 Hugging Face 模型库中的模型（请根据您的需求替换为其他模型）
repo_id = "google/flan-t5-xxl"  # 可以查看 https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads 以获取其他选项

# 创建 HuggingFaceHub 对象，设置模型的一些参数（例如温度和生成的最大长度）
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)

# 调用模型并生成结果
result = llm("1+1=")
print(result)
# -> 2
