from flask_app.models.productos import Producto

print("Obtener un producto por nombre")

producto = Producto.get_by_name("Laptop HP")
print(f"Producto: {producto.nombre}")