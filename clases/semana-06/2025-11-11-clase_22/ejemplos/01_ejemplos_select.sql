-- Seleccionar todas las columnas
SELECT *
FROM tweets;

SELECT *
FROM usuarios;

-- Seleccionar columnas especificas
SELECT nombre, apellido
FROM usuarios;

-- Buscar registros con WHERE
SELECT *
FROM usuarios
WHERE id=5;

-- Where con OR / AND
SELECT *
FROM usuarios
WHERE id=5 OR id=4;

SELECT *
FROM usuarios
WHERE id > 3 AND id < 10;

-- Obtener datos con LIKE
SELECT *
FROM usuarios
WHERE nombre LIKE '%e';

SELECT *
FROM usuarios
WHERE nombre_usuario LIKE '%15';

SELECT *
FROM usuarios
WHERE nombre_usuario LIKE '%\_%\_%';

-- Ordenar obtencion de registos con ORDER BY
SELECT nombre, apellido
FROM usuarios
ORDER BY nombre DESC;

-- Where y ORDER BY
SELECT *
FROM tweets
WHERE tweet LIKE "%navidad%"
ORDER BY created_at DESC;


-- Limitar resultados
SELECT *
FROM tweets
LIMIT 3;

SELECT *
FROM tweets
LIMIT 3
OFFSET 2;

SELECT *
FROM tweets
LIMIT 2, 3;
