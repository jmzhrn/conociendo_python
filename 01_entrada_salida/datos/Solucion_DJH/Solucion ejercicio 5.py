#Escribir archivo
texto = input("Escribe tu texto: ")

with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto)

print("El texto se guardo correctamente.")