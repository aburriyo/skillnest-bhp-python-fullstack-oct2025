class TarjetaCredito:
    banco = "Banco Internacional de Programadores"
    
    def __init__(self, limite_credito):
        self.limite_credito = limite_credito

tarjeta1 = TarjetaCredito(20000)
tarjeta2 = TarjetaCredito(30000)

print(f"Tarjeta 1: {tarjeta1.banco}")
print(f"Tarjeta 2: {tarjeta2.banco}")

print("-----------")

# De esta forma cambiamos el atributo de la clase
# para un solo objeto
tarjeta1.banco = "Banco Nacional de Python"
tarjeta1.cuenta = "Corriente" # No hacer

print(f"Tarjeta 1: {tarjeta1.banco}")
print(f"Tarjeta 1: {tarjeta1.cuenta}")
print(f"Tarjeta 2: {tarjeta2.banco}")

print("-----------")

# Cambiar el atributo de la clase (para todos los objetos)
TarjetaCredito.banco = "Banco Nacional de Desarrolladores Full Stack"

print(f"Tarjeta 1: {tarjeta1.banco}")
print(f"Tarjeta 2: {tarjeta2.banco}")
