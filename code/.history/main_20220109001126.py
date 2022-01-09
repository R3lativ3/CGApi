from flask import Flask, jsonify
from config import config
from common.connection import getConnection
from controller.RutasController import rutas_blueprint 

app = Flask(__name__)
app.register_blueprint(rutas_blueprint, url_prefix='/rutas')

@app.route("/")
def index():
    cnx = getConnection()
    cursor = cnx.cursor()

    query = ("select * from rutas")
    cursor.execute(query)
    data = cursor.fetchall()

    return jsonify({'rutas': data})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()