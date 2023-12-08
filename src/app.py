from flask import Flask
from decouple import config
from modelo.clientes import Modelocliente
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  " hola mundo "

#mostrar todos los clientes
@app.route("/clientess", methods=['GET'])
def listar_estudiantes():
    resul=Modelocliente.listar_cliente()
    return resul

#buscar solo un estudiante
@app.route("/clientes/:<codigo>", methods=['GET'])
def lista_estudiante(codigo):
    resul=Modelocliente.lista_cliente(codigo)
    return resul

#registrar estudiante
@app.route("/clientes",methods=['POST'])
def guardar_cliente():
    resul=Modelocliente.registrar_cliente()
    return resul


#actualizar estudiante
@app.route("/clientes/:<codigo>",methods=['PUT'])
def ctualizar_cliente(codigo):
    resul=Modelocliente.actualizar_cliente(codigo)
    return resul


#eliminar estudiante
@app.route("/clientes/:<codigo>",methods=['DELETE'])
def elimineycion_cliente(codigo):
    resul=Modelocliente.eliminar_cli(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Página no Encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0')
