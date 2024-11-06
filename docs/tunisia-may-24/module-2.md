# Introduction to Generative AI and LLMs

### Module Objectives
This module provides foundational knowledge on Large Language Models (LLMs), covering key concepts such as pretraining, foundational models, and adapting LLMs through fine-tuning. Additionally, the module introduces various open-source and proprietary LLMs currently available on the market.

### Module Topics
- **Introducing Generative AI**  
  - What is Generative AI?
  - How Gen AI differs from Predictive AI.
  - Brief history of Gen AI.
  - Capabilities of Gen AI and major use cases.
  - Different categories of Gen AI (LLMs, image generators, video generators).

- **Understanding Large Language Models (LLMs)**  
  - Overview and history of language models—LLMs vs. SLMs.
  - Categories of LLMs: Foundation models and other concepts.
  - Building LLMs: Transformer architecture and sequence-to-sequence architectures.
  - Overview of common LLMs: OpenAI models, Mistral AI, Llama, Gemini, and others.
  - Adapting and customizing LLMs: fine-tuning, pre-training, RLHF.

- **Building and Evaluating LLM Apps**  
  - Key concepts for LLM apps: prompt engineering, prompt-tuning, vector embeddings, RAG.
  - Ecosystem of commercial and open-source tools for building LLM apps (e.g., LangChain).
  - Customizing LLMs for specific use cases: prompt engineering, RAG, fine-tuning, RLHF.
  - Selecting and evaluating LLMs and LLM apps.

- **Deploying LLM Apps with LangChain**  
  - Overview of LangChain features and capabilities.
  - Preprocessing and loading data in LangChain.
  - Working with different LangChain agents (e.g., SQL).
  - Deploying LangChain applications (e.g., with Streamlit, WhatsApp, and web apps).
  - Evaluating LangChain apps.

### Practical Labs

- **Lab 1: Demonstration of Building an LLM App with Commercial Tools (OpenAI)**  
  Since participants won’t have access to a paid OpenAI subscription, the instructor will demonstrate available capabilities for building LLM apps. The lab will include:
  - Exploring OpenAI features using the ChatGPT GUI (paid version), showing functionalities and how to create assistants.
  - Demonstrating a simple RAG-based chatbot using the OpenAI playground.
  - Demonstrating a simple RAG-based chatbot using the OpenAI API.

- **Lab 2: Building LLM Apps Using LangChain (RAG-Based Chatbot)**  
  Participants will use provided documents to build a RAG-based app with an open-source LLM to query the documents. The output will be a Streamlit app for sharing. Tasks include:
  - Setting up the development environment and installing required packages.
  - Preparing source data (e.g., health documents).
  - Setting up a vector database.
  - Preprocessing documents and loading them into the vector database.
  - Integrating with an LLM (including selecting the LLM).
  - Developing the user interface in Streamlit.
  - Deploying and testing the app.

### Case Study
- **Agricultural Information Q&A System in Malawi**  
  A RAG-based chatbot deployed in Malawi answers questions from Agricultural Extension workers. This example app uses ChatGPT (OpenAI) integrated with agricultural documents from Malawi and is deployed on WhatsApp.

### Assessment
- **Build an LLM App with LangChain**  
  Participants will receive a notebook to create an app that answers questions based on their selected website. Additionally, a quiz with five multiple-choice questions will be administered.
