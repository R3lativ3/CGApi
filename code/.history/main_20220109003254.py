from flask import Flask, jsonify, request
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

@app.route("/post", methods=['POST'])
def post():
    req_data = request.get_json()
    departamento = req_data['departamento']
    print(departamento)
    add_departamento = ("INSERT INTO departamentos "
                        "(departamento) "
                        "VALUES (%s)")
    cnx = getConnection()       #obtengo conexion
    cursor = cnx.cursor()       #cursor
    cursor.execute(add_departamento, (departamento))    #ejecuto el insert, seguido de lo que insertare
    id = cursor.lastrowid                                 #obtener id insertado                    
    print(id)         
    cnx.commit()                                          #guardar cambios
    cursor.close()                                        #cerrar conexion y cursor
    cnx.close()
    return jsonify({'id': id})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()