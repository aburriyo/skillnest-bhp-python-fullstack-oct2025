texto = "Hola Mundo"

texto_mayuscula = texto.upper()

texto_ocurrencias = texto.count("o")

texto_split = texto.split()

texto_reemplazado = texto.replace("Mundo", "Python")

texto_comienza_con = texto.startswith("Mundo")

print(texto)
print(texto_mayuscula)
print(texto_ocurrencias)
print(type(texto_ocurrencias))

print(texto_split)
print(type(texto_split))

print(texto_reemplazado)

print(texto_comienza_con)