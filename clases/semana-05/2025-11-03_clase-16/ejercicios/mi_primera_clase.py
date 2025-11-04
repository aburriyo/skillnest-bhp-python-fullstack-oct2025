class Usuario: # Camel Case
    def __init__(self, nombre: str, apellido: str, email: str, limite_credito: int = 300, saldo_a_pagar: int=0): # método constructor
        # Atributos de Instancia
        self.banco = "Estado"

        # Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_a_pagar = saldo_a_pagar
    
    def __str__(self):
        return f"Esto es una clase de Usuario"
    

usuario_1 = Usuario(nombre="Diego", apellido="Canales", email="diego@email.com", limite_credito=1500)
usuario_2 = Usuario(nombre="Juan", apellido="Canales", email="juan@email.com")
usuario_3 = Usuario(nombre="Gloria", apellido="Canales", email="gloria@email.com")

print("Usuario 1")
print(f"Mi nombre es {usuario_1.nombre} {usuario_1.apellido}, mi correo es {usuario_1.email}, limite crédito : {usuario_1.limite_credito}")

print("Usuario 2")
print(f"Mi nombre es {usuario_2.nombre} {usuario_2.apellido}, mi correo es {usuario_2.email}, limite crédito : {usuario_2.limite_credito}")

print("Usuario 3")
print(f"Mi nombre es {usuario_3.nombre} {usuario_3.apellido}, mi correo es {usuario_3.email}, limite crédito : {usuario_3.limite_credito}")


print(f"Usuario 1: {usuario_1}")
