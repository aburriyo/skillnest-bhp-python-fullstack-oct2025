from flask import Flask, render_template, request, redirect
from flask_app.models.productos import Producto

app = Flask(__name__)

@app.route("/productos")
def mostrar_productos():
    productos = Producto.get_all()
    print(productos)  # Ver en la terminal
    #return render_template("dashboard.html", todos_productos=productos)
    return render_template("dashboard_tabla.html", todos_productos=productos)


@app.route("/productos/<int:id>")
def ver_producto(id):
    data = {"id": id}
    producto = Producto.get_one(data)
    return render_template("ver_producto.html", producto=producto)

@app.route("/productos/nuevo")
def nuevo_producto():
    return render_template("nuevo_producto.html")


@app.route("/productos/crear", methods=["POST"])
def crear_producto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    descripcion = request.form["descripcion"]
    categoria_id = request.form["categoria_id"]

    data = {
        "nombre": nombre,
        "precio": precio,
        "descripcion": descripcion,
        "categoria_id": categoria_id
    }

    print("Estamos recibiendo")
    id_nuevo_producto = Producto.save(datos=data)
    
    return redirect("/productos")


if __name__ == "__main__":
    app.run(debug=True)
