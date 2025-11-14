from flask_app.models.productos import Producto

data = {
    "nombre": "Iphone Pro Max 1000",
    "precio": 10000,
    "descripcion": "Chapado en oro",
    "categoria_id": 1,
}


id_nuevo_producto = Producto.save(datos=data)
print(f"ID nuevo producto: {id_nuevo_producto}")