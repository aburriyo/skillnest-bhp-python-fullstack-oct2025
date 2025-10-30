print(list(range(5)))

print("Bucle solo fin")
for i in range(5):
    print(f"indice: {i}")


print("Bucle inicio fin")
for i in range(2, 6):
    print(f"indice: {i}")

print("Bucle inicio, fin, paso")
for i in range(0, 10, 2):
    print(f"indice {i}")

# for cadenas de texto
mensaje = "Hola Mundo"

for caracter in mensaje:
    print(caracter)

# contador de vocales
contador_vocales = 0
for caracter in mensaje:
    if caracter.lower() in "aeiou":
        contador_vocales = contador_vocales + 1 # contador_vocales+=1
        print(f"Encontré la vocal {caracter}")
print(f"La cantidad de vocales son {contador_vocales}")

# recorrer listas

frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")


for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")


# while

# contraseña_correcta = "python123"
# intento = ""
# while intento != contraseña_correcta:
#     intento = input("Ingresa la contraseña: ")

# print("¡Acceso concedido!")

while True:
    print("Bucle infinito")