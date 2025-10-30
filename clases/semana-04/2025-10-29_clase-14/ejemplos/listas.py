numeros = [3, 1, 4, 1, 5, 9, 2]
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

largo_lista = len(numeros)
print(largo_lista)

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#               [0,    1,   2,   3,   4,   5,   6,   7  , 8,   9]

print(letras[2:5])

print(letras[:4])

print(letras[6:])

print(letras[0:10:2]) # 0:100:2 también se ejecuta sin error

letras_invertidas = letras[::-1]
print(letras_invertidas)

print(letras)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)
print(lista2 + lista1)

print(lista1 * 3)

print(lista1 + [3])