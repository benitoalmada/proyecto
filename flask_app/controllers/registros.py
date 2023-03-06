from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.actividad import Actividad
from flask_app.models.usuario import Usuario
from flask_app.models.registro import Registro






@app.route('/registro/nuevo', methods=['POST'])
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


@app.route('/registro/mostrar/<int:id>')
def show_registro(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("mostrar_resultados.html", registro=Registro.trae_uno(data), user=Usuario.traer_id(user_data),  actividad=Actividad.trae_uno(data))


@app.route('/registro/modificar/<int:id>')
def modificar_registro(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar.html", modificar_registro=Registro.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actualizar/registro', methods=['POST'])
def actualizar_registro():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Registro.validar_registro(request.form):
        return redirect('/registro')
    data = {
        "fecha": request.form["fecha"],
        "hora": request.form["hora"],
        "puntaje": request.form["puntaje"],
        "duracion": (request.form["duracion"]),
        "id": request.form['id']
    }
    Actividad.actualizar(data)
    return redirect('/pagina1')


@app.route('/registro/eliminar/<int:id>')
def eliminar_actividad(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Actividad.eliminar(data)
    return redirect('/pagina1')
