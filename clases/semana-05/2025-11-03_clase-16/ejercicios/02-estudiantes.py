class Estudiante:
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 edad: int,
                 curso: str = "Python Full Stack",
                 nota_promedio: float = 0.0,
                 activo: bool = True):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
        self.nota_promedio = nota_promedio
        self.activo = activo
    
    def saludar(self): # Acá estoy utilizando atributos del objeto instanciado, entonces necesito el self
        print(f"Mi nombre es {self.nombre} {self.apellido}")

    def cumpleanios(self):
        self.edad = self.edad + 1

    @staticmethod # métodos estáticos
    def feliz_cumpleanios(): # Acá no estoy utilizando ningun atributo del objeto instanciado, entonces no necesito el self
        print("Feliz Cumpleaños!")

estudiante = Estudiante(nombre="Diego",
                        apellido="Canales",
                        edad=99)
print(f"Nota promedio {estudiante.nota_promedio}")

estudiante.nota_promedio = 1.4
print(f"Nota promedio {estudiante.nota_promedio}")

# Llamamos al método saludar
estudiante.saludar()


estudiante_2 = Estudiante(nombre="Juan",
                        apellido="Perez",
                        edad=999)
estudiante_2.saludar()
estudiante.feliz_cumpleanios()

print(estudiante_2.edad)
estudiante_2.cumpleanios()
print(estudiante_2.edad)