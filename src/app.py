import json
from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
conexion=MySQL(app)

@app.route('/clientes', methods=["GET"])
def listar_clientes():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM clientes"
        cursor.execute(sql)
        datos=cursor.fetchall()
        #print(datos)
        clientes = []
        for fila in datos:
            cliente = {'id_clientes': fila[0], 'nombres': fila[1], 'nit': fila[2], 'correo': fila[3], 'contra': fila[4]}
            clientes.append(cliente)
        return jsonify({'clientes':clientes,'mensaje':"Listo!"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

@app.route('/clientes/<id_clientes>', methods=["GET"])
def leer_clientes(id_clientes):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM clientes where id_clientes='{0}'".format(id_clientes)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            cliente = {'id_clientes': datos[0], 'nombres': datos[1], 'nit': datos[2], 'correo': datos[3], 'contra': datos[4]}
            return jsonify({'cliente':cliente, 'mensaje': ":3"})
        else:
            return jsonify({'mensaje':"No fue encontrado"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

@app.route('/clientes', methods=["POST"])
def agregar_cliente():
    #print(request.json)
    try:
        cursor=conexion.connection.cursor()
        sql = "INSERT INTO clientes(id_clientes,nombres,nit,correo,pass) VALUES({0},'{1}','{2}','{3}','{4}')".format(request.json['id_clientes'],request.json['nombres'],request.json['nit'],request.json['correo'],request.json['pass'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Registrado con exito"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

@app.route('/clientes/<id_clientes>', methods=["PUT"])
def actualizar(id_clientes):
    try:
        cursor=conexion.connection.cursor()
        sql = "UPDATE clientes set nombres='{0}',nit='{1}',correo='{2}',pass='{3}' where id_clientes='{4}'".format(request.json['nombres'],request.json['nit'],request.json['correo'],request.json['pass'],id_clientes)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Actulizado con exito"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

@app.route('/clientes/<id_clientes>', methods=["DELETE"])
def eliminar(id_clientes):
    try:
        cursor=conexion.connection.cursor()
        sql = "DELETE FROM clientes where id_clientes= '{0}'".format(id_clientes)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Eliminado con exito"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

def PagNoExiste(error):
    return "<h1>No existe</h1>",

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, PagNoExiste)
    app.run()