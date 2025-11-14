from flask_app.models.usuarios import Usuario

usuarios = Usuario.get_all()

print("Obtener todos los usuarios")

print(usuarios)

print("Obtener un usuario")

data = {"id": 1}
usuario = Usuario.get_one(data)
print(f"Usuario: {usuario.nombre} {usuario.apellido}")