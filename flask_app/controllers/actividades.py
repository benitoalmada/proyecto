from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.actividad import Actividad
from flask_app.models.usuario import Usuario
from flask_app.models.registro import Registro


@app.route('/actividad')
def actividad():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('agregar.html', usuario=Usuario.traer_id(data))
    #return render_template('agregar.html', usuarios=usuario.Usuario.traer_todo())

@app.route('/actividad/agregar', methods=['POST'])
def crear_actividad():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Actividad.validar_actividad(request.form):
        return redirect('/actividad')
    data = {
        "actividad": request.form["actividad"],
        "nro": request.form["nro"],
        "description": request.form["description"],
        "nivel": request.form["nivel"]
    }
    Actividad.save(data)
    return redirect('/pagina1')


@app.route('/actividad/hacer/<int:id>')
def hacer_actividad(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("actividad1.html", actividad=Actividad.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actividad/modificar/<int:id>')
def modificar_actividad(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar.html", modificar_actividad=Actividad.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actualizar/actividad', methods=['POST'])
def actualizar_actividad():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Actividad.validar_actividad(request.form):
        return redirect('/actividad')
    data = {
        "actividad": request.form["actividad"],
        "nro": request.form["nro"],
        "description": request.form["description"],
        "nivel": (request.form["nivel"]),
        "id": request.form['id']
    }
    Actividad.actualizar(data)
    return redirect('/pagina1')


@app.route('/actividad/eliminar/<int:id>')
def eliminar_actividad(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Actividad.eliminar(data)
    return redirect('/pagina1')


@app.route('/registro/agregar', methods=['POST'])
def crear_registro():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Registro.validar_registro(request.form):
        return redirect('/actividad')
    data = {
        "fecha": request.form["fecha"],
        "hora": request.form["hora"],
        "puntaje": request.form["puntaje"],
        "duracion": request.form["duracion"],
        "user_id": session["user_id"]
    }
    Registro.save(data)
    return redirect('/actividad')

@app.route('/actividad/mostrar/<int:id>')
def mostrar_registro(id):
            if 'user_id' not in session:
                return redirect('/inisesion')
            data = {
                "id": id
            }
            user_data = {
                "id": session['user_id']
            }
            return render_template("mostrar_resultados.html", actividad_reg=Registro.traer_todo_actividades(data), user=Usuario.traer_id(user_data))
