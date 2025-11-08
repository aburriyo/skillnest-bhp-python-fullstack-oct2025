from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'clave-temporal-desarrollo')

print(f"Clave: {app.secret_key}")

@app.route("/") # GET
def home():
    mensaje = "<ul><li>Hola</li></ul>"
    return render_template("index.html", mensaje=mensaje)


@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    rol = request.form["rol"]
    print(f"El nombre del usuario es {nombre}")
    print(f"El email del usuario es {email}")
    print(f"El rol del usuario es {rol}")

    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["rol_usuario"] = rol

    return redirect("/exito")

@app.route("/exito")
def exito():
    return render_template("exito.html")

@app.route("/mostrar_usuario")
def mostrar_usuario():
    nombre = session["nombre_usuario"]
    email = session["email_usuario"]
    print(f"Usuario {nombre}, Email: {email}")
    return f"Usuario {nombre}, Email: {email}"


@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)