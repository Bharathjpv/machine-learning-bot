import sys
import os
import config
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models.openai import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader

from src.entity.config_entity import (
    ChainConfig,
    MemoryConfig,
    OpenAIConfig,
)
from src.exception import CustomException
from src.logger import logging
from src.constants import *

openai_api_key = config.DevelopmentConfig.OPENAI_KEY

class BotChain:
    def __init__(self):
        self.openai_config = OpenAIConfig()

        self.memory_config = MemoryConfig()

        self.chain_config = ChainConfig()

    def get_llm_chain(self) -> ConversationalRetrievalChain:
        """
        This function initializes and returns a ConversationalRetrievalChain object for OpenAI language
        model using Chroma database as retriever and ConversationBufferMemory as memory.

        Returns:
          The method `get_llm_chain` returns an instance of the `ConversationalRetrievalChain` class.
        """
        logging.info("Entered get_llm_chain method of LLMChain class")

        try:
            loader = TextLoader('text.txt')
            docs = loader.load()

            logging.info("Load the Text documet for generate emebeddings")

            db = FAISS.from_documents(documents=docs, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key))

            logging.info(
                f"Initialised FAISS with OpenAIEmbeddings as the embedding function"
            )

            self.memory = ConversationBufferMemory(**self.memory_config.__dict__)

            logging.info(
                f"Initialised ConversationBufferMemory with {self.memory_config.__dict__} as the parameters"
            )

            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=ChatOpenAI(**self.openai_config.__dict__),
                retriever=db.as_retriever(),
                memory=self.memory,
                get_chat_history=lambda h: h,
                **self.chain_config.__dict__,
            )

            logging.info(
                f"Initialised ConversationalRetrievalChain for OpenAI LLM with {self.openai_config.__dict__} as parameters"
            )

            logging.info("Exited get_llm_chain method of LLMChain class")

            return qa_chain

        except Exception as e:
            raise CustomException(e, sys)
        
    def SaveConversation(self, filepath: str)-> None:
        """
        This function saves the conversation in a text file
        
        input: filepath

        Returns: None
        """
        try:

            os.makedirs(CONVERSATION_DIR, exist_ok=True)
            with open(filepath , 'w') as f:
                f.writelines(self.memory.load_memory_variables({})['chat_history'])
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def ClearHistory(self) -> None:
        '''
        This function clear the memory of conversation chain and make way to a new chain
        '''
        try:
            self.memory.clear()

        except Exception as e:
            raise CustomException(e, sys)
