from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import complemento

class Taco:
    def __init__(self, data):
        self.id = data['id']
        self.tortilla = data['tortilla']
        self.guiso = data['guiso']
        self.salsa = data['salsa']
        self.restaurante_id = data['restaurante_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.complementos = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id) VALUES(%(tortilla)s, %(guiso)s, %(salsa)s, %(restaurante_id)s);"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tacos;"
        tacos_en_bd = connectToMySQL('esquema_tacos').query_db(query)
        tacos = []
        for taco in tacos_en_bd:
            tacos.append(cls(taco))
        return tacos
    
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM tacos WHERE id = %(id)s;"
        taco_en_db = connectToMySQL('esquema_tacos').query_db(query,datos)

        return cls(taco_en_db[0])
    
    @classmethod
    def update(cls, datos):  # TODO: agregar campo restaurante_id
        query = "UPDATE tacos SET tortilla=%(tortilla)s, guiso=%(guiso)s, salsa=%(salsa)s WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM tacos WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)


    @classmethod
    def get_taco_y_complementos(cls, datos):
        
        # TODO: implementar función (es todo al reves)
        pass
