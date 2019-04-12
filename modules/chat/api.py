from flask import Flask,jsonify,request
from modules.chat import Chat

todos = {}

@Chat.route("/chat", methods=['POST'])
def chat():
    data = request.data.decode()
    print(data)
    if "再见" in data and "您好" in data:
        todos["result"] = "天气不错。"
    elif "再见" in data:
        todos["result"] = "再见了您内。"
    elif "您好" in data:
        todos["result"] = "您好，您吃了吗？"
    return jsonify(todos)
