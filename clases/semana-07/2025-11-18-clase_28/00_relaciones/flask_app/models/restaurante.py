from flask_app.config.mysqlconnection import connectToMySQL

class Restaurante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.tacos = []



    @classmethod
    def save(cls, datos):
        query = "INSERT INTO restaurantes (nombre) VALUES(%(nombre)s);"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM restaurantes;"
        restaurantes_en_bd = connectToMySQL('esquema_tacos').query_db(query)
        restaurantes = []
        for restaurante in restaurantes_en_bd:
            restaurantes.append(cls(restaurante))
        return restaurantes
    
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM restaurantes WHERE id = %(id)s;"
        restaurante_en_db = connectToMySQL('esquema_tacos').query_db(query,datos)

        return cls(restaurante_en_db[0])

    @classmethod
    def update(cls, datos):
        query = "UPDATE restaurantes SET nombre=%(nombre)s WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM restaurantes WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
