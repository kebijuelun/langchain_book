# 🦜️ LangChain Quick Guide

![langchain book](./figures/langchain_book.png)

Welcome to the accompanying code repository for "LangChain Quick Guide: Building LLM Applications from 0 to 1".
- Book Link: [LangChain Quick Guide](https://item.jd.com/10099611004672.html)


## ✅ Table of Contents
1. Introduction to Large Language Models
2. Introduction to LangChain
3. Model Invocation
4. Model Input/Output
5. Data Connection
6. Memory Modules
7. Chains
8. Agents
9. Practice: Chatbots
10. Practice: Code Understanding
11. Practice: Retrieval-Enhanced Generation

## 🚀 Code Download
Please download the code repository and initialize submodules first, to ensure you have all the necessary code and resources for this book:
```bash
git clone https://github.com/kebijuelun/langchain_book.git
cd langchain_book
git submodule update --init --recursive
```


## 💻 Environment Setup


### Recommended Environment for This Book
It is recommended to run the code of this book in a Linux environment (such as Ubuntu 20.04), using Conda, Python, and LangChain libraries, to enjoy the convenience of installation. Although Windows also supports all code execution, considering the potential local model deployment requirements (such as CUDA, CuDNN installation), the Linux system can provide a more stable and compatible environment. This helps to seamlessly run examples in the book and support more advanced application development.

Both pip and Conda installation methods are provided, but **using Conda is strongly recommended** as Conda can provide a more consistent, controlled environment.

### LangChain Python Environment Installation (conda)

Conda is a powerful tool for package and environment management. To install Conda on Linux, first download and install Miniconda:
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Activate the Conda environment, and create a LangChain environment:
```bash
source ~/miniconda3/bin/activate
conda env create -f langchain.yml # Run this command in the root directory of the accompanying code repository for this book
source ~/miniconda3/bin/activate langchain
```
This ensures you have a clean environment with all necessary libraries, avoiding dependency issues.

### LangChain Python Environment Installation (pip)

To install LangChain, execute in the Linux terminal:
```bash
pip install langchain==0.0.268
pip install openai
```
Note that this will install the most basic requirements of LangChain. To install various models providers and related libraries included in LangChain, follow the commands below:
```bash
pip install langchain[all]==0.0.268
# Linux zsh users: pip install "langchain[all]==0.0.268"
```
Here, the LangChain version is fixed to 0.0.268 to ensure the replication of examples in the book. Note that if you wish to use a newer version of LangChain, you can upgrade with the following command:
```bash
pip install langchain --upgrade
```
Be aware that upgrading may cause incompatibilities with the code in the book. Other library dependencies can be installed with the following command:
```bash
pip install -r requirements.txt
```


### 😀 Confirming Environment Setup is Successful
- Most LangChain examples are based on the OpenAI Large Language Model API. To run the code, first set up the OpenAI API key. An OpenAI API key can be applied for at the [OpenAI API keys official website](https://platform.openai.com/account/api-keys).
```bash
export OPENAI_API_KEY="sk-xxx" # Replace with your applied key
python3 2.Introduction_to_LangChain/2.Environment_Setup_Guide/1.openai_helloworld.py
# -> Hello! How can I assist you today?
```
If the environment setup is successful, the above message will be printed normally.


## 🤗 Acknowledgments
This code repository is built with reference to the following libraries:

- [LangChain](https://github.com/langchain-ai/langchain/)
- [weblangchain](https://github.com/langchain-ai/weblangchain)