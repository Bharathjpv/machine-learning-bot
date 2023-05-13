# Machine Learning Bot

This is an ai powered bot.
Need a data sample like in `text.txt` using which it generates embeddings and saves them in FAISS for further use.

Given the question/user form the input bot will look for the answers associated with certain keywords in the `text.txt` file and returns the relevent answer.

When the conversations end bot atomatically saves the conversation in `.txt` file and deletes the history/memory of the bot and starts fresh again

## How to run?

Clone this repo
```bash
git clone https://github.com/Bharathjpv/machine-learning-bot.git
```
Install all the requirements (create vertual environament if required)
```bash
pip install -r requirements.txt
```
set openai api key as environamental variable
```bash
export OPENAI_API_KEY="your-openai-api-key"
```
run the flask application
```bash
python app.py
```

You can acces the frontend in any browser with port number `5000`

 http://localhost:5000/


sample outresponses

![example](https://github.com/Bharathjpv/machine-learning-bot/assets/84281655/cd8f3417-2720-4d5d-aa96-2e90302aaf22)
