import os
import sys


from src.logger import logging
from src.exception import CustomException
from src.api.chain import BotChain
from src.constants import *

conversation_file = os.path.join(CONVERSATION_DIR, CONVERSATION_FILE_NAME)

bot = BotChain()
logging.info("Instance of chatbot created")
qa_chain = bot.get_llm_chain()

def generateChatResponse(prompt):
    '''
    This function takes the prompt as input and retutns the generated response of the bot

    parameters

    prompt: input form the user

    returns: response from the bot
    '''
    logging.info("Entered the generateChatResponse of aiapi")

    try:
        answer = qa_chain(prompt)['answer']
        logging.info("Response generated for bot")
        return answer

    except Exception as e:
        raise CustomException(e, sys)

def SaveFile():
    bot.SaveConversation(conversation_file)
    bot.ClearHistory()

    # print("--------" + memory.load_memory_variables({})['chat_history'])
