class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.energia = 100
    
    def ladrar(self):
        print("{self.nombre} está ladrando")
    
    def correr(self):
        self.energia = self.energia - 20
        return self
    
    def dormir(self):
        self.energia = self.energia + 50
        if self.energia + 50 > 100:
            self.energia = 100
        return self