import streamlit as st
from langchain.llms import OpenAI
import os
from pathlib import Path
from langchain_community.llms import HuggingFaceEndpoint, HuggingFaceHub
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, ConversationChain, RetrievalQA, RetrievalQAWithSourcesChain
from langchain_openai import ChatOpenAI, OpenAI
from langchain.memory import ChatMessageHistory, ConversationBufferMemory, ConversationSummaryMemory

# Document Loaders and Text Splitter
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, HNLoader, UnstructuredHTMLLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

# Vector Embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.runnables import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# App Logic 
st.title('🦜🔗 RAG Based Chatbot')

OPENAI_API_KEY = st.sidebar.text_input('OpenAI API Key', type='password')
DIR_WD = Path("/Users/dunstanmatekenya/Google Drive/My Drive/GenAI-Course/Mod2-LLM-Overview/")
DIR_DATA = DIR_WD.joinpath("data")
DIR_DOCS = Path("/Users/dunstanmatekenya/Google Drive/My Drive/GenAI-Course/Public Health Documents")
FILE_TU_COVID_RESPONSE = DIR_DOCS.joinpath("who_wou_apr_2024.pdf")

def load_pdf_docs(pdf_file):
    # Load the PDF
    loader = PyPDFLoader(pdf_file)
    data = loader.load()

    chunk_size = 400
    chunk_overlap = 100

    rc_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap = chunk_overlap)
    docs = rc_splitter.split_documents(data)
    
    return docs

def add_documents2vectordb(embedding_model, pdf_file, vectordb_dir):
    
    # Load and split the file
    docs = load_pdf_docs(pdf_file)
    
    # Create embeddings
    embedding_model = OpenAIEmbeddings(openai_api_type=OPENAI_API_KEY)


    vectordb = Chroma(persist_directory=vectordb_dir, embedding_function=embedding_model)

    vectordb.persist()
    docstorage = Chroma.from_documents(docs, embedding_model)
    
    return docstorage

def generate_response(input_text):
    embedding_function = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    docstorage = add_documents2vectordb(embedding_model=embedding_function, 
                                        pdf_file=str(FILE_TU_COVID_RESPONSE), 
                                        vectordb_dir=str(DIR_DATA))
    print('Done with Preparing Documents')
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_API_KEY, 
               temperature=0.7)
    qa = RetrievalQAWithSourcesChain.from_chain_type(llm=llm,chain_type="stuff", 
                                                     retriever=docstorage.as_retriever())
    results = qa({"question": "{}".format(input_text)},
             return_only_outputs=True)
    print(results)
    st.info(results)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the situation of drought in the Amazon forest?')
    submitted = st.form_submit_button('Submit')
    if not OPENAI_API_KEY.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and OPENAI_API_KEY.startswith('sk-'):
        generate_response(text)