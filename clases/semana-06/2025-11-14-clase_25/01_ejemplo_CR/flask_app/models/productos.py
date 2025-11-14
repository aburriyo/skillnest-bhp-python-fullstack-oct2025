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
        query = "SELECT * FROM productos;"
        resultados = connectToMySQL("tienda").query_db(query)

        objetos = []
        for data in resultados:
            objeto = cls(data)
            objetos.append(objeto)
        return objetos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM productos WHERE id = %(id)s"
        resultado = connectToMySQL("tienda").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def get_by_id(cls, id: int):
        data = {"id": id}
        query = "SELECT * FROM productos WHERE id = %(id)s"
        resultado = connectToMySQL("tienda").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return False
    
    @classmethod
    def get_by_name(cls, nombre: str):
        data = {"nombre": nombre}
        query = "SELECT * FROM productos WHERE nombre = %(nombre)s"
        resultado = connectToMySQL("tienda").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return False


    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO productos
            (nombre, precio, descripcion, categoria_id)
            VALUES (%(nombre)s, %(precio)s, %(descripcion)s, %(categoria_id)s)
        """
        nuevo_id = connectToMySQL('tienda').query_db(query, datos)
        return nuevo_id