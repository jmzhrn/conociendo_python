# Leer numero de archivo

with open("numero.txt", "r", encoding="utf-8") as archivo:
    numero = int(archivo.read())

print("El numero es:", numero)