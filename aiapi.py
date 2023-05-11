# import openai
# import config

# openai.api_key = config.DevelopmentConfig.OPENAI_KEY

# def generateChatResponse(prompt):

#     messages = []
#     messages.append({"role": "system", "content": "You are a helpful assistant."})

#     question = {}
#     question['role'] = 'user'
#     question['content'] = prompt
#     messages.append(question)
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
#     try:
#         ans = response['choices'][0]['message']['content'].replace('\n', '<br>')
#     except:
#         ans = "No response. Try again"

#     return ans
import config

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

openai_api_key = config.DevelopmentConfig.OPENAI_KEY

template = """Your name is alex and you help customers of Happy face online retail to solve their issues regarding their orders.

%MESSAGE
{message}

YOUR RESPONSE:
"""

prompt_template = PromptTemplate(input_variables=["message"], template=template)
llm = OpenAI(temperature=1, openai_api_key=openai_api_key)

def generateChatResponse(prompt):
    chain = LLMChain(llm=llm, prompt=prompt_template)

    answer = chain.run(prompt)
    return answer.replace('\n', '<br>')