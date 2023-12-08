from modelo.Coneccion import conexion2023
from flask import jsonify, request

def buscar_cliente(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM cliente WHERE cod_c = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            estu = {'cod_c': datos[0], 'nombre': datos[1],
                       'apellido': datos[2], 'domicilio': datos[3]}
            return estu
        else:
            return None
    except Exception as ex:
            raise ex


class Modelocliente():
    @classmethod
    def listar_cliente(self):
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            datos = cursor.fetchall()
            estudiantes = []

            for fila in datos:
                estu = {' cod_c': fila[0],
                       'nombre': fila[1],
                       'apellido': fila[2],
                       'domicilio': fila[3]}
                estudiantes.append(estu)

            conn.close()

            return jsonify({'clientes': estudiantes, 'mensaje': "clientes listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})

    @classmethod
    def lista_cliente(self,codigo):
        try:
            usuario = buscar_cliente(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "cliente encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_cliente(self):
        try:
            usuario = buscar_cliente(request.json['ci_e'])
            if usuario != None:
                return jsonify({'mensaje': "Codigo de comercio  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT cliente values(%s,%s,%s,%s)', (request.json['ci_e'], request.json['nombre_e'], request.json['apell_pat_e'],
                                                                            request.json['apell_mat_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def actualizar_cliente(self,codigo):
        try:
            usuario = buscar_cliente(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE cliente SET nombre=%s, apellido=%s, domicilio=%s WHERE cod_c=%s""",
                        (request.json['nombre_e'], request.json['apell_pat_e'], request.json['apell_mat_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def eliminar_cli(self,codigo):
        try:
            usuario = buscar_cliente(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM cliente WHERE cod_c = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})