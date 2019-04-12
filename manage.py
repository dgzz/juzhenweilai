from flask import Flask, jsonify

app = Flask(__name__)

# 注册蓝图
from modules.add import Add
app.register_blueprint(Add)

from modules.date import Date
app.register_blueprint(Date)

from modules.chat import Chat
app.register_blueprint(Chat)
if __name__ == '__main__':
    app.run(debug=True)
