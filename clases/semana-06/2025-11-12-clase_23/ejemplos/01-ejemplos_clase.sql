USE tienda;
SELECT * FROM usuarios;
SELECT * FROM direcciones;

SELECT COUNT(*)
FROM usuarios;


SELECT COUNT(DISTINCT ciudad) FROM direcciones;

SELECT COUNT(DISTINCT edad) FROM usuarios;

SELECT *
FROM productos;

SELECT SUM(precio)
FROM productos;

SELECT *
FROM pedidos;

SELECT SUM(total)
FROM pedidos
WHERE fecha >= '2024-02-01';

SELECT AVG(edad)
FROM usuarios;

SELECT AVG(precio) -- dasdasda
FROM productos; -- dasdasda

SELECT MAX(precio)
FROM productos;

SELECT MIN(edad), MAX(edad) FROM usuarios;
