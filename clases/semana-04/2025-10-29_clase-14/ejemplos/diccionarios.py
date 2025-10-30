from pprint import pprint # de la libreria (from) pprint importa pprint -> es una función

persona = {} # diccionario vacio

print(persona)

persona["nombre"] = "Juan"

print(persona)

persona["edad"] = 28
persona["ciudad"] = "Lima"

print(persona)

mensaje = f"Mi nombre es {persona["nombre"]} y mi edad es {persona["edad"]}"

print(mensaje)

persona["edad"] = 29
print(persona["edad"])

# datos complejos

persona["tecnologias"] = ["Python", "HTML", "CSS", "JS"]

persona["instructor"] = {"nombre": "Diego", "ciudad": "Temuco"}

pprint(persona)

# métodos

# print(persona["telefono"]) esto da error, persona no tiene la clave "telefono"
print(persona.get("telefono")) # no se cae el programa, pero retorna None

estudiante = {"nombre": "Ana",
              "edad": 25,
              "curso": "Python",
              "telefono": "+5612345678"}
print(estudiante.get("telefono"))
print(estudiante.keys())
print(estudiante.items())
# [('nombre', 'Ana'), ('edad', 25), ('curso', 'Python'), ('telefono', '+5612345678')]

estudiante.update({"ciudad": "Arica"})

pprint(estudiante)

print("nombre" in estudiante)

print("region" in estudiante)