from flask import Flask, request, jsonify
from test import OpenAIresponse


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Pls ask your question </h1>"

@app.route("/response", methods = ["POST"])
def ask_question():
    data = request.get_json()

    if 'question' not in data:
        return jsonify({"error": "No question provide, pls provide question"}), 400
    
    question = data["question"]

    answer = OpenAIresponse(question)

    return jsonify({"question": question, "answer": answer})


if __name__ =="__main__":
    app.run(debug=True)





