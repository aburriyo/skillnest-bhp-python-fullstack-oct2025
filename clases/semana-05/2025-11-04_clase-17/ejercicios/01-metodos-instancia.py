class Perro:
    # Init 1
    def __init__(self, nombre, raza, edad, energia=100):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.energia = energia
    
    # Init 2
    # def __init__(self, nombre, raza, edad):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.energia = 100

    def ladrar(self):
        print(f"{self.nombre} está ladrando")
        return self
    
    def correr(self):
        self.energia = self.energia - 20
        print(f"La energia restante es {self.energia}")
        return self
    
    def dormir(self):
        # self.energia = self.energia + 50
        # if self.energia > 100:
        #     self.energia = 100
        
        energia_aux = self.energia + 50
        if energia_aux > 100:
            self.energia = 100
        else:
            self.energia = self.energia + 50



perro_1 = Perro("Firulais", "Kiltro", 14)
# perro_1 = Perro("Firulais", "Kiltro", 14)
# perro_1.energia = 1000
