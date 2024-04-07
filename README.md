# 🦜️ LangChain 简明讲义

## <div align="center"><b><a href="README.md">简体中文</a> | <a href="README_EN.md">English</a></b></div>

![langchain book](./figures/langchain_book.png)

欢迎来到 《LangChain 简明讲义：从 0 到 1 构建 LLM 应用程序》书籍的配套代码仓库。
- 书籍链接：[LangChain 简明讲义](https://item.jd.com/10099611004672.html)


## ✅ 书籍目录
1. 大语言模型简介
2. LangChain 简介
3. 模型调用
4. 模型输入输出
5. 数据连接
6. 记忆模块
7. 链
8. 智能体
9. 实践：对话机器人
10. 实践：代码理解
11. 实践：检索增强生成

## 🚀 代码下载
请先下载代码库并初始化子模块，确保有本书所有必需的代码和资源：
```bash
git clone https://github.com/kebijuelun/langchain_book.git
cd langchain_book
git submodule update --init --recursive
```


## 💻 环境配置


### 本书推荐运行环境
推荐在 Linux 环境（如 Ubuntu 20.04）下运行本书代码，利用 Conda、Python、LangChain 等库，以享受安装便捷性。虽然 Windows 也支持全部代码运行，但鉴于可能的本地模型部署需求（如 CUDA、CuDNN 安装），Linux 系统能提供更稳定、兼容的环境。这有助于无缝运行书中示例并支持更高级的应用开发。

提供 pip 和 Conda 两种安装方法，但**强烈推荐使用 Conda**，因为 Conda 能够提供更一致、可控的环境。

### LangChain python 运行环境安装 (conda)

Conda 是包管理和环境管理的强大工具。在 Linux 上安装 Conda，首先下载并安装 Miniconda：
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

激活 Conda 环境，并创建 LangChain 环境：
```bash
source ~/miniconda3/bin/activate
conda env create -f langchain.yml # 直接在本书配套代码库根目录中运行该命令
source ~/miniconda3/bin/activate langchain
```
这将确保您有一个包含所有必要库的干净环境，避免依赖问题。

### LangChain Python 运行环境安装 (pip)

要安装 LangChain，请在 Linux 终端执行：
```bash
pip install langchain==0.0.268
pip install openai
```
需要注意的是这将安装 LangChain 的最基本要求，如果需要安装 LangChain 所包含的各种模型提供商和数据存储等相关的库则需要按照以下命令进行安装
```bash
pip install langchain[all]==0.0.268
# Linux zsh 用户：pip install "langchain[all]==0.0.268"
```
这里固定 LangChain 版本为 0.0.268 版本以确保能够成功复现本书中的示例。请注意，如果您想使用更新的 LangChain 版本，可以运行以下命令来升级：
```bash
pip install langchain --upgrade
```
请注意，升级可能导致与书中代码不兼容。其他库依赖可通过以下命令安装：
```bash
pip install -r requirements.txt
```


### 😀 确认环境安装正常
- LangChain 示例大多数基于 OpenAI 大型语言模型 API。运行代码首先需设置 OpenAI API 秘钥。OpenAI API 秘钥可以在 [OpenAI API keys 官网](https://platform.openai.com/account/api-keys) 申请。
```bash
export OPENAI_API_KEY="sk-xxx" # 替换为读者申请的秘钥
python3 2.LangChain简介/2.环境安装指南/1.openai_helloworld.py
# -> Hello! How can I assist you today?
```
环境安装成功会正常打印以上信息。


## 🤗 致谢
本代码库参考以下库进行构建:

- [LangChain](https://github.com/langchain-ai/langchain/)
- [weblangchain](https://github.com/langchain-ai/weblangchain)