from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

conexion = connectToMySQL("tienda")

query_join = """
SELECT 
    usuarios.id,
    usuarios.nombre,
    COUNT(pedidos.id) AS cantidad_pedidos,
    SUM(pedidos.total) AS total_gastado,
    AVG(pedidos.total) AS promedio_gastado
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id
WHERE pedidos.fecha >= '2024-02-01'
GROUP BY usuarios.id, usuarios.nombre
HAVING COUNT(pedidos.id) >= 2;
"""


resultados = conexion.query_db(query_join)

conexion = connectToMySQL("tienda")

resultados = conexion.query_db("SELECT * FROM productos;")

for registro in resultados:
    pprint(registro)
    break
