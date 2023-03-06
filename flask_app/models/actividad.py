from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Actividad:
    def __init__(self, data):
        self.id = data['id']
        self.actividad = data['actividad']
        self.nro = data['nro']
        self.description = data['description']
        self.nivel = data['nivel']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO actividades (actividad, nro, description, nivel, created_at, updated_at) VALUES (%(actividad)s, %(nro)s, %(description)s,  %(nivel)s, now(),now());"
        return connectToMySQL('bdproyecto').query_db(query,data)
   
    @classmethod
    def traer_todo(cls):
        query = "SELECT id, actividad, nro, description, nivel, created_at, updated_at FROM actividades;"
        toda_actividad = []
        results = connectToMySQL('bdproyecto').query_db(query)
        for row in results:
            toda_actividad.append(cls(row))
            print(row)
        return toda_actividad
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM actividades;"
        results =  connectToMySQL('bdproyecto').query_db(query)
        all_actividades= []
        for row in results:
            all_actividades.append( cls(row) )
        return all_actividades
    

    @classmethod
    def trae_uno(cls, data):
        query = "SELECT r.id, r.actividad, r.nro, r.description, r.nivel, r.created_at, r.updated_at FROM actividades r WHERE r.id = %(id)s;"
        results = connectToMySQL('bdproyecto').query_db(query, data)
        return cls(results[0])

    @classmethod
    def actualizar(cls,data):
        query = "UPDATE actividades SET actividad=%(actividad)s,nro=%(nro)s,description=%(description)s,nivel=%(nivel)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdproyecto').query_db(query, data)
    @classmethod
    def eliminar(cls,data):
        query  = "DELETE FROM actividades WHERE id = %(id)s;"
        return connectToMySQL('bdproyecto').query_db(query, data)

    @staticmethod
    def validar_actividad(actividad):
        is_valid = True
        if len(actividad['actividad']) < 2:
            flash("El nombre de la actividad debe tener por lo menos 2 caracteres", "actividad")
            is_valid = False
        if len(actividad['nro']) < 0:
            flash("El número debe tener por lo menos 1 digito positivo", "actividad")
            is_valid = False
        if len(actividad['description']) < 5:
            flash("La descrición debe tener por lo menos 5 caracteres", "actividad")
            is_valid = False
        if len(actividad['nivel']) < 1:
            is_valid = False
            flash("Asigne un nivel","actividad")

        return is_valid
    @classmethod
    def traer_todo_actividades(cls):
            query = "SELECT r.fecha, r.hora, r.puntaje, r.duracion, u.id, u.first_name, a.id, a.actividad FROM registros r JOIN actividades a ON a.id=r.actividad_id 	join usuarios u on u.id=r.usuario_id 	WHERE  r.usuario_id = '2' and r.actividad_id='2'"
            toda_registro_actividad = []
            results = connectToMySQL('bdproyecto').query_db(query)
            for row in results:
                toda_registro_actividad.append(cls(row))
                print(row)
            return toda_registro_actividad


class Registro:
    def __init__(self, data):
        self.id = data['id']
        self.actividad = data['actividad']
        self.nro = data['nro']
        self.description = data['description']
        self.nivel = data['nivel']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fecha = data['fecha']
        self.hora = data['hora']
        self.puntaje = data['puntaje']
        self.duracion = data['duracion']

    @classmethod
    def traer_todo_actividades(cls):
        query = "SELECT r.fecha, r.hora, r.puntaje, r.duracion, u.id, u.first_name, a.id, a.actividad FROM registros r JOIN actividades a ON a.id=r.actividad_id 	join usuarios u on u.id=r.usuario_id 	WHERE  r.usuario_id = '2' and r.actividad_id='2'"
        toda_registro_actividad = []
        results = connectToMySQL('bdproyecto').query_db(query)
        for row in results:
                toda_registro_actividad.append(cls(row))
                print(row)
        return toda_registro_actividad
