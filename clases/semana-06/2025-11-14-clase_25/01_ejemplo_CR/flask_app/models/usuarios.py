from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    def __str__(self):
        return f"id: {self.id} | nombre: {self.nombre} | apellido: {self.apellido} | email: {self.email}"
    
    def __repr__(self):
        return f"Usuario(id: {self.id} | nombre: {self.nombre} | apellido: {self.apellido} | email: {self.email})"
    
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL("tienda").query_db(query)

        objetos = []
        for data in resultados:
            objeto = cls(data)
            objetos.append(objeto)
        return objetos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultado = connectToMySQL("tienda").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return False

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultado = connectToMySQL("tienda").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return False

    



