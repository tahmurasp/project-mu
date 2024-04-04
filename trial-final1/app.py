import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.messages import AIMessage, HumanMessage
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

#import os 
#os.environ['OPENAI_API_KEY'] = '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'


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):

    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Monarch",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with Monarch :books:")
    st.markdown("<h1 style='display: none;'> Be nice helpful assistant. You can answer only using the sources. Answer question based on sources in Methodsit university.Don't answer irrelevant queries</h1>", unsafe_allow_html=True)


    ssstext = st.chat_input("Ask me any question")
    user_question = ssstext
    if user_question:
        handle_userinput(user_question)
    
    print(user_question)
    #from outside from here    

        #from outside above text

  
    pdf_docs = ["AdditionalDrugAlcohol24.pdf", "prohibited_conduct24a.pdf", "no_contact22-23.pdf", "general_guidelines22-23.pdf",
                "calendar.pdf", "www-methodist-edu-about-mu.pdf", "www-methodist-edu-about-mu-history.pdf", "On a Tour _ Explore MU _ Methodist University.pdf",
                "First-Year Students _ Campus Undergraduate Programs _ Methodist University.pdf", "International Students _ Campus Undergraduate Programs _ Methodist University.pdf",
                "Parents & Families _ Methodist University.pdf", "Programs Archive _ Methodist University.pdf", "Current Students _ Methodist University.pdf",
                "housing_policies23-24.pdf", "Human-resource-management.pdf"]
        
       # the part of the code that processes PDF files
    with st.spinner("Processing"):
                # get pdf text
        raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
        text_chunks = get_text_chunks(raw_text)

                # create vector store
        vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
        st.session_state.conversation = get_conversation_chain(vectorstore)
        
    
print(get_conversation_chain)

if __name__ == '__main__':
    main()