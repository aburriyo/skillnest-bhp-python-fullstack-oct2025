-- Mostrar tweets
SELECT *
FROM tweets;

SELECT *
FROM usuarios;

INSERT INTO tweets (tweet, usuario_id)
VALUES ("Hola Skillnest este es un nuevo tweet", 5);

INSERT INTO tweets (tweet, usuario_id, created_at, updated_at)
VALUES ("Este tweet si tiene fechas de creacion", 5, "2025-11-11", "2025-11-11");

INSERT INTO usuarios (nombre, apellido, nombre_usuario, fecha_nacimiento)
VALUES ('Carlos', 'Rodríguez', 'carlos_r', '1990-05-15');

INSERT INTO usuarios (nombre, apellido, nombre_usuario, fecha_nacimiento)
VALUES ('Diego', 'Rodríguez', 'carlos_r', '1990-05-15');

ALTER TABLE usuarios
MODIFY COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE tweets
MODIFY COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

ALTER TABLE usuarios
MODIFY COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;