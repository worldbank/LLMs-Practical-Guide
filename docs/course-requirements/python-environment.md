# Python Environment Configuration
In this section, we provide the minimal Python packages required to complete the programming exercises in this course. We are saying minimal because for some of the project work, you may need extra packages

## Python Installation
We will be using Python 3.12 for this course. Please refer to the installation options below. 

- **Recommended: Installation with Anaconda**. [Download Anaconda](https://www.anaconda.com/download). For more details about Anaconda, refer to this [blog post](https://www.anaconda.com/blog).

- **Alternative: Installation from Python Website**
[Download Python](https://www.python.org/downloads/)

## Python IDE
An IDE (Integrated Development Environment) is a software application that provides programmers with tools for software development, such as a source code editor, compiler, build automation, and debugging tools. Popular Python IDEs include Jupyter Notebook, VS Code, and PyCharm.

### Jupyter Notebook and Google Colab

After installing Python, you can proceed to install Jupyter Notebook, the default IDE for data science and scientific computing. Jupyter Notebook allows you to write code and include documentation with Markdown. If you installed Python via the Anaconda distribution, Jupyter Notebook and other commonly used Python packages come pre-installed, saving you additional setup steps.

In addition to the local Jupyter Notebook installation with Anaconda, you can also use a similar environment on hosted servers like Google Colab. Google Colab is an online Jupyter Notebook accessible via the cloud, offering free GPUs for working with LLMs and other AI-based Python programs.

### Full-Featured IDEs
While Jupyter Notebooks are excellent for interactive data science work, this course focuses on building a chatbot, which requires a fully-featured IDE. Below are some commonly used IDEs:

> 🚀 **VS Code**: Recommended IDE for this course.See [installation instructions](https://code.visualstudio.com).

**Other IDEs**
- **Notepad++**
- **PyCharm**

## Python Environment Setup
### Major Packages 
For the most part, we’ll install packages as needed. However, here’s a list of core packages we’ll require:

1.Transformers

2.Pytorch

3.HuggingFace

4.Langchain 

The full list of required packages is provided in the ```requirements.txt``` file. 

### Python Environment Setup
#### Create Virtual Environment
Create a Python virtual environment to use for this project. The Python version used when this was developed was 3.12.  The code below creates a virtual environment and also installs all the Python packages we need for this tutorial
```
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```
#### Setup ```.env``` file 
This file is important for keeping your API keys and other secrets
```
# OpenAI
OPENAI_API_KEY="<Put your token here>"
# Hugging Face
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"

# Twilio Credentials
TWILIO_ACCOUNT_SID="<Put your token here>"
TWILIO_AUTH_TOKEN="<Put your token here>"
TWILIO_NUMBER="<Put your token here>"

# PostgreSQL connection details
DB_USER = "<Put your token here>"
DB_PASSWORD = "<Put your token here>"
```

