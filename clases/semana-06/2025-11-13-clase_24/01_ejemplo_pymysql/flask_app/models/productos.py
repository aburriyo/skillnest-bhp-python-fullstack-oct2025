from flask_app.config.mysqlconnection import connectToMySQL

class Producto:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]
        self.descripcion = data["descripcion"]
        self.categoria_id = data["categoria_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM producto;"
        resultados = connectToMySQL("tienda").query_db(query)

        objetos = []
        for data in resultados:
            objeto = cls(data)
            objetos.append(objeto)
        return objetos