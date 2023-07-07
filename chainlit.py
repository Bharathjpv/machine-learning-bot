import chainlit as cl

import aiapi
import config
from langchain.prompts import PromptTemplate

from src.api.prompt import Prompt
abc=0


prompt = Prompt().GeneratePrompt()
@cl.on_message
async def main(message: str):
    # Your custom logic goes here...
    if abc == 0:
        prompt = Prompt().GeneratePrompt()
        prompts = message
        query = prompt.format(human_input= prompts, chat_history= [])
        abc = 1
        answer= aiapi.generateChatResponse(query)
        # Send a response back to the user
    else:
        prompts = message
        res = {}
        answer= aiapi.generateChatResponse(query)

    await cl.Message(
        content=f"Received: {answer}",
    ).send()

