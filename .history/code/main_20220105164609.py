from re import DEBUG
from flask import Flask, json, jsonify
from config import config
from common.connection import getConnection
app = Flask(__name__)


@app.route("/")
def index():
    cnx = getConnection()
    cursor = cnx.cursor()

    query = ("select * from rutas")
    cursor.execute(query)
    data = cursor.fetchall()

    return jsonify({'rutas': })



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()