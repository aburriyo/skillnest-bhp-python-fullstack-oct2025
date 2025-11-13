from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

conexion = connectToMySQL("tienda")

resultados = conexion.query_db("SELECT * FROM productos;")
pprint(resultados)
