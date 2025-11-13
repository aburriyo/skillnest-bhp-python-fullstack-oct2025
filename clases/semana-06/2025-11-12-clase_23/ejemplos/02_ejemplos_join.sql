USE tienda;

SELECT *
FROM usuarios
JOIN direcciones ON usuarios.id = direcciones.usuario_id;

SELECT nombre, apellido, email, edad, calle, ciudad, codigo_postal
FROM usuarios
JOIN direcciones ON usuarios.id = direcciones.usuario_id;

SELECT * 
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;

-- ejemplo muchos a muchos paso 1
SELECT * 
FROM pedidos
JOIN pedidos_has_productos ON pedidos.id = pedidos_has_productos.pedido_id
JOIN productos ON productos.id = pedidos_has_productos.producto_id;


-- Left JOIN

SELECT *
FROM usuarios
LEFT JOIN direcciones ON usuarios.id = direcciones.usuario_id;

SELECT usuarios.nombre, resenas.comentario
FROM usuarios
LEFT JOIN resenas ON usuarios.id = resenas.usuario_id
WHERE usuarios.id = 2 OR usuarios.id = 6;

SELECT usuarios.nombre, productos.nombre AS producto, resenas.comentario
FROM usuarios
LEFT JOIN resenas ON usuarios.id = resenas.usuario_id
LEFT JOIN productos ON resenas.producto_id = productos.id
WHERE usuarios.id = 2 OR usuarios.id = 6;


SELECT 
    p1.nombre AS producto1,
    p2.nombre AS producto2
FROM productos p1
JOIN productos p2 ON p1.categoria_id = p2.categoria_id AND p1.id != p2.id
WHERE p1.id = 1;

SELECT 
    p1.nombre AS producto1,
    p2.nombre AS producto2,
    c.nombre AS categoria
FROM productos p1
JOIN productos p2 ON p1.categoria_id = p2.categoria_id AND p1.id != p2.id
JOIN categorias c ON p1.categoria_id = c.id
WHERE p1.id = 1;


-- Group BY

SELECT 
    usuarios.nombre,
    pedidos.id,
    pedidos.fecha
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;

SELECT 
    usuarios.id,
    usuarios.nombre,
    COUNT(pedidos.id) AS cantidad_pedidos,
    SUM(pedidos.total) AS total_gastado,
    AVG(pedidos.total) AS total_gastado
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id
WHERE pedidos.fecha >= '2024-02-01'
GROUP BY usuarios.id, usuarios.nombre
HAVING COUNT(pedidos.id) >= 2;



