from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)
