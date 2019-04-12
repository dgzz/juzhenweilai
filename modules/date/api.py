from flask import Flask,jsonify
from modules.date import Date
import datetime
import time
app = Flask(__name__)
# 注册蓝图
app.register_blueprint(Date)
todos = {}

@Date.route("/get_date", methods=['GET'])
def get_date():
    times = datetime.datetime.now()
    times = datetime.datetime.strftime(times,'%Y-%m-%d')
    todos['date'] = times
    return jsonify(todos)
