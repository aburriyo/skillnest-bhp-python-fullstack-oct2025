from flask import Flask, render_template, request, redirect
from flask_app.models.usuarios import Usuario

app = Flask(__name__)

@app.route("/usuarios")
def mostrar_usuarios():
    usuarios = Usuario.get_all()
    return render_template("dashboard_tabla.html", usuarios=usuarios)

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("nuevo_usuario.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    edad = int(request.form["edad"])

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "edad": edad
    }
    id_nuevo_usuario = Usuario.save(datos=data)
    
    return redirect("/usuarios")


if __name__ == "__main__":
    app.run(debug=True)
