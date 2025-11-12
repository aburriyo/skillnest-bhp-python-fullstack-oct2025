SELECT *
FROM tweets;

SELECT *
FROM favoritos;

UPDATE tweets
SET tweet = "Modifique este tweet soy hacker"
WHERE id = 14;

UPDATE usuarios
SET nombre = "Maria", apellido = "Lopez", nombre_usuario = "maria_lopez"
WHERE id = 7;

SELECT *
FROM tweets
WHERE usuario_id >= 3 AND usuario_id <= 5;

UPDATE tweets
SET tweet = "Te hackie la cuenta gg"
WHERE usuario_id >= 3 AND usuario_id <= 5;

DELETE FROM tweets
WHERE id = 13;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM usuarios;
