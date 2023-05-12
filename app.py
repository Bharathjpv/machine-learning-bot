from flask import Flask, render_template, request, jsonify
import aiapi
import config
import openai
from langchain.prompts import PromptTemplate

app = Flask(__name__)
app.config.from_object(config.config['development'])

template = """
Imagine your a customer care excutive and your name is Alex from Happy Face online retail.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(input_variables=["chat_history","human_input"], template=template)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompts = request.form['prompt']
        query = prompt.format(human_input= prompts, chat_history= [])

        res = {}
        res['answer'] = aiapi.generateChatResponse(query)
        return jsonify(res), 200

    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")