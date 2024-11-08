# Programming Activities
This document outlines the programming activities for the course, focusing on hands-on projects to apply the concepts learned. The document is organized into two main sections: an introduction to LLM capabilities and LangChain, followed by a practical exercise on deploying a chatbot with Streamlit.

## 1. LLM Foundations-understanding the ML Process 

## 2.Introducing LLM Capabilities and LangChain

In this section, we explore the foundational capabilities of Large Language Models (LLMs) and how they can be applied in real-world scenarios. By leveraging LLMs, you can build applications such as chatbots, document analyzers, and automated support systems.

### 2.1 Understanding LLM Capabilities
LLMs are capable of generating human-like text, answering questions, summarizing content, and even performing tasks like sentiment analysis and named entity recognition. These models can process and interpret vast amounts of textual data, making them ideal for a variety of applications across domains.

### 2.2 Introducing LangChain
LangChain is a powerful framework that simplifies the process of integrating LLMs into applications. It provides modular components and utility functions to create chains (pipelines) that combine different tasks, such as prompting, data processing, and memory management, all within a cohesive system. LangChain makes it easier to build applications that require complex interactions with language models, including:

- **Prompt Engineering**: Designing effective prompts to achieve desired responses from the LLM.
- **Data Handling**: Loading, processing, and storing large document corpora.
- **Chain Management**: Creating workflows that link multiple steps, such as data loading, prompt generation, and response handling.

### 2.3 Building Applications with LangChain
LangChain supports various use cases, including:

1. **QA Chatbots**: Answering user questions based on specific datasets.
2. **Document Analysis**: Extracting information, summarizing content, or classifying documents.
3. **Automated Support Systems**: Handling customer service or FAQ queries.

In this course, we will apply these capabilities to build a QA chatbot using LangChain, deploy it on Streamlit, and explore its functionality through real-world examples.

## 3 Deploying a Chatbot on Streamlit
In this activity, you will use the knowledge gained from the LangChain Tutorial to explore a chatbot deployed on Streamlit. You will deploy this app on your computer and interact with it.

### 3.1 About Streamlit

As discussed in the lectures, Streamlit is a platform that enables data scientists to deploy dynamic, data-based apps. It’s ideal for prototyping demonstration apps and sharing them with stakeholders before full-scale production deployment.

### 3.2 Initial Setup and Getting the Chatbot Files

1. **Get OpenAI and Hugging Face API Credentials**  
   The chatbot uses OpenAI models, so you’ll need to sign up for an OpenAI developer account and obtain an API key. For a step-by-step guide on creating an OpenAI API key, search for instructions on ChatGPT. Similarly, create a Hugging Face account and obtain an API token.

2. **Try the Chatbot on Streamlit Community Cloud**  
   Before downloading anything, you can try the chatbot on the Streamlit Community Cloud with just the OpenAI and Hugging Face keys.

3. **Download or Clone the Project Repository**  
   To get the project files on your computer, either clone the GitHub repository (if familiar with Git) or download the repository as a zipped file.

### 3.3 Deploying the Streamlit App Locally

1. **Unzip and Navigate to the Project Folder**  
   Once unzipped, open the project folder and follow the instructions on the GitHub page to deploy the chatbot.

2. **Follow steps on GitHub project repository**. [Streamlit app repo](https://github.com/worldbank/RAG-Based-ChatBot-Example)


3. **Install Required Packages**  
   The `requirements.txt` file contains a list of all required packages. If you encounter a missing package error, try installing the package again (ensuring your virtual environment is activated).

4. **Run the App Locally**  
   Run the app with the following command:  
   ```bash
   streamlit run streamlit_app.py
   ```
5. **Test and Check**. When deployed locally, you can browse the files being used in the app.

### 3.4 Explore Important Scripts in the App

The essential components for building a chatbot with LangChain are organized into distinct, modular Python scripts. Let’s explore some of these elements. You can use VS Code or your preferred text editor for this task.

#### 3.4.1 Loading Files
In real-life applications, you may need to load hundreds of documents, requiring a versatile function for file loading. This project includes two types of loaders:
- **`remote_loader.py`**: For loading documents from websites.
- **`local_loader.py`**: For loading documents from the local `data` folder.

#### 3.4.2 Document Splitting
The `splitter.py` module uses the `RecursiveCharacterTextSplitter` strategy, with a chunk size of 1000 and an overlap of 0. This method helps in breaking down large documents into manageable sections for processing.

#### 3.4.3 Prompt Chains
In the `full_chain.py`, `base_chain.py`, and `rag_chain.py` modules, you’ll find configurations for the specific LLM models and prompting strategies used. The project utilizes OpenAI chat models, with customized chains designed to guide interactions effectively.

#### 3.4.4 Memory Management
Memory management strategies are also implemented to optimize the chatbot’s performance, particularly for long interactions or when processing large datasets.