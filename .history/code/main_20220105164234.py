from re import DEBUG
from flask import Flask
from config import config
from common.connection.py import getConnection()
app = Flask(__name__)



@app.route("/")
def index():
    return "hola"



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()