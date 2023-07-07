from flask import Flask, render_template, request, jsonify
import aiapi
import config
from langchain.prompts import PromptTemplate

from src.api.prompt import Prompt

app = Flask(__name__)
app.config.from_object(config.config['development'])
abc = 0
# template = """
# Your a customer care excutive and your name is Alex from Happy Face online retail.
# Your name is alex.

# {chat_history}
# Human: {human_input}
# Chatbot:"""

# prompt = PromptTemplate(input_variables=["chat_history","human_input"], template=template)

prompt = Prompt().GeneratePrompt()
@app.route('/', methods = ['POST', 'GET'])
def index():
    global abc
    if request.method == 'POST':
        
        if abc == 0:
            prompts = request.form['prompt'] 
            query = prompt.format(human_input= prompts, chat_history= [])
            abc = 1
            res = {}
            res['answer'] = aiapi.generateChatResponse(query)
            
            return jsonify(res), 200
        else:
            prompts = request.form['prompt']
            res = {}
            res['answer'] = aiapi.generateChatResponse(prompts)
            return jsonify(res), 200
    
    return render_template('index.html', **locals())

@app.route('/reset', methods = ['POST', 'GET'])
def reset():
    global abc
    aiapi.SaveFile()
    abc = 0
    return render_template('index.html', **locals())

if __name__ == "__main__":

    app.run(host='0.0.0.0', port="5000")