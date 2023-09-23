from flask import Flask, render_template, request, jsonify
from chat import chatbot
import json

app = Flask(__name__)

data_path = 'a.json'

with open(data_path,'r') as file:
    data = json.load(file)

@app.get("/")
def index_get():

    return render_template("index.html")
@app.post("/predict")
def predict():
    text = request.get_json().get ("message")
    # TODO: check if text is valid
    response = chatbot(data,text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True,port=5000)