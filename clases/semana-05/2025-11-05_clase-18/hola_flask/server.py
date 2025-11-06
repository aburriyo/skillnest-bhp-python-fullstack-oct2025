from flask import Flask, render_template

app = Flask(__name__)    # Crea una instancia de Flask

@app.route('/')          # Define la ruta "/"
def hola_mundo():
    return '¡Hola Mundo!'  # Retorna un mensaje

@app.route('/contacto')          # Define la ruta "/contacto"
def contacto():
    return 'Mi contacto es bla bla bla'  # Retorna un mensaje

@app.route('/contacto/numero')          # Define la ruta "/contacto/numero"
def contacto_numero():
    return 'Mi numero es bla bla bla'  # Retorna un mensaje

@app.route('/saludo/<nombre>')
def saludo(nombre):
    print(nombre)
    return f"Hola {nombre}!"

@app.route("/saludo/<nombre>/<int:num>")
def hola_cantidad(nombre, num):
    return f"Hola {nombre}" * num

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}"


# @app.route("/bienvenido")
# def bienvenido():
#     return render_template("index.html")


@app.route('/bienvenido')
def bienvenido():
    repite = 10 * 5
    return render_template('index.html', 
                          cancion="dale a tu cuerpo alegría macarena", 
                          repite=repite)


if __name__=="__main__":
    app.run(debug=True)    # Ejecuta en modo debug