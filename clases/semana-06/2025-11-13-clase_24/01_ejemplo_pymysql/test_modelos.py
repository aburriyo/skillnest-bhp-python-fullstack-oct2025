from flask_app.models.usuarios import Usuario

usuarios = Usuario.get_all()

print(usuarios)
