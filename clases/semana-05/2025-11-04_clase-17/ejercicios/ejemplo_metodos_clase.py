class Estudiante:
    escuela = "Escuela de Programadores"
    todos_los_estudiantes  = []
    
    def __init__(self, escuela, edad, nota):
        self.escuela = escuela
        self.edad = edad
        self.nota = nota
        Estudiante.todos_los_estudiantes.append(self)
    
    @classmethod
    def cambiar_escuela(cls, nuevo_nombre):
        cls.escuela = nuevo_nombre
    
    @classmethod
    def promedio_general(cls):
        total = 0
        for estudiante in cls.todos_los_estudiantes:
            total += estudiante.nota
        promedio = total / len(cls.todos_los_estudiantes)
        return promedio
