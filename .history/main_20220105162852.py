from re import DEBUG
from flask import Flask
import code.config as config
app = Flask(__name__)



@app.route("/")
def index():
    return "hola"




if __name__ == '__main__':
    app.config_class(DEBUG = True)
    app.run()