from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Registro:
    def __init__(self, data):
        self.id = data['id']
        self.fecha = data['fecha']
        self.hora = data['hora']
        self.puntaje = data['puntaje']
        self.duracion = data['duracion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.first_name = data['first_name']
        self.actividad = data['actividad']
        self.actividad_id = data['actividad_id']
        self.usuario_id_actividad = data['usuario_id_actividad']



    @classmethod
    def save(cls, data):
        query = "INSERT INTO registros (fecha, hora, puntaje, duracion, created_at,updated_at, usuario_id, actividad_id, usuario_id_actividad) VALUES (%(fecha)s, %(hora)s, %(puntaje)s,  %(duracion)s, now(),now(), %(usuario_id)s, %(actividad_id)s, %(usuario_id_actividad)s;"
        return connectToMySQL('bdproyecto').query_db(query, data)

    @classmethod
    def traer_todo(cls):
        query = "SELECT r.id, r.fecha, r.hora, r.puntaje, r.duracion, r.created_at, r.updated_at u.first_name, r.usuario_id FROM registros r LEFT JOIN usuarios u on u.id=r.usuario_id;"
        toda_registro= []
        results = connectToMySQL('bdproyecto').query_db(query)
        for row in results:
            toda_registro.append(cls(row))
            print(row)
        return toda_registro

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM registros;"
        results = connectToMySQL('bdproyecto').query_db(query)
        all_registro = []
        for row in results:
            all_registro.append(cls(row))
        return all_registro

    @classmethod
    def trae_uno(cls, data):
        query = "SELECT r.id, r.fecha, r.hora, r.puntaje, r.duracion, r.created_at, r.updated_at FROM registros r WHERE r.id = %(id)s;"
        results = connectToMySQL('bdproyecto').query_db(query, data)
        return cls(results[0])

    @classmethod
    def actualizar(cls, data):
        query = "UPDATE registros SET fecha=%(fecha)s,hora=%(hora)s,puntaje=%(puntaje)s,duracion=%(duracion)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdproyecto').query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM registros WHERE id = %(id)s;"
        return connectToMySQL('bdproyecto').query_db(query, data)

    @staticmethod
    def validar_registro(registro):
        is_valid = True
        if len(registro['fecha']) < 2:
            flash(
                "Se debe ingresar la fecha", "registro")
            is_valid = False
        if len(registro['hora']) < 0:
            flash("La hora debe tener por lo menos 1 digito positivo", "registro")
            is_valid = False
        if len(registro['puntaje']) < 5:
            flash("El puntaje debe tener por lo menos 5 caracteres", "registro")
            is_valid = False
        if len(registro['duracion']) < 1:
            is_valid = False
            flash("debe contener duración", "registro")

        return is_valid

    @classmethod
    def traer_todo_actividades(cls):
        query = "SELECT r.id, r.fecha, r.hora, r.puntaje, r.duracion, r.created_at, r.updated_at FROM registros r WHERE r.id = 1;"
       
        toda_registro_actividad = []
        results = connectToMySQL('bdproyecto').query_db(query)
        for row in results:
            toda_registro_actividad.append(cls(row))
            print(row)
        return toda_registro_actividad
