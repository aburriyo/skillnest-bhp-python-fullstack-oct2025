class Perro:
    def __init__(self, nombre: str, raza: str, edad: int):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

perro_1 = Perro(nombre="Max", raza="Labrador", edad=5)
perro_2 = Perro(nombre="Coraje", raza="Cobarde", edad=4)
perro_3 = Perro(nombre="Hades", raza="Pastor Alemán", edad=8)

print(f"Nombre: {perro_1.nombre} | Raza: {perro_1.raza} | Edad {perro_1.edad}")
print(f"Nombre: {perro_2.nombre} | Raza: {perro_2.raza} | Edad {perro_2.edad}")
print(f"Nombre: {perro_3.nombre} | Raza: {perro_3.raza} | Edad {perro_3.edad}")
