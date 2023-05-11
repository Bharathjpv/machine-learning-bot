from flask import Flask, render_template, request, jsonify
import aiapi
import config
import openai

app = Flask(__name__)
app.config.from_object(config.config['development'])

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        print('---------------')
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200

    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")