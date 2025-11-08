from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/") # GET
def home():
    return render_template("index.html")

@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    print(f"El nombre del usuario es {nombre}")
    print(f"El email del usuario es {email}")
    return redirect("/exito")

@app.route("/exito")
def exito():
    return render_template("exito.html")


if __name__ == "__main__":
    app.run(debug=True)