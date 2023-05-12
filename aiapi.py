# import config

# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

# openai_api_key = config.DevelopmentConfig.OPENAI_KEY

# template = """Your name is alex and you help customers of Happy face online retail to solve their issues regarding their orders.

# %MESSAGE
# {message}

# YOUR RESPONSE:
# """

# prompt_template = PromptTemplate(input_variables=["message"], template=template)
# llm = OpenAI(temperature=1, openai_api_key=openai_api_key)

# def generateChatResponse(prompt):
#     chain = LLMChain(llm=llm, prompt=prompt_template)

#     answer = chain.run(prompt)
#     return answer.replace('\n', '<br>')

import config

from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

openai_api_key = config.DevelopmentConfig.OPENAI_KEY

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

loader = TextLoader('text.txt')
docs = loader.load()

db = FAISS.from_documents(docs, embeddings)

memory = ConversationBufferMemory(memory_key='chat_history', return_messages=False)

qa_chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=.5, openai_api_key=openai_api_key,request_timeout=15),
            retriever=db.as_retriever(),
            memory=memory,
            get_chat_history=lambda h: h,
            chain_type='stuff'
        )

def generateChatResponse(prompt):

    answer = qa_chain(prompt)['answer']
    return answer
