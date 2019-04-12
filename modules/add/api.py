from flask import Flask,jsonify
from flask import request
import json
from modules.add import Add

todos = {}

@Add.route("/add", methods=['POST'])
def adds():
    data = request.data.decode()
    data = json.loads(data)
    sum = 0
    for dicts in data.values():
        for dict in dicts:
            for value in dict.values():
                sum += value
    todos['result'] = sum
    return jsonify(todos)
