#Ejercicio 1
texto = "Hola Mundo"

# Alineado a la derecha en 20 caracteres
print(f"{texto:>20}")

# Truncamiento en el cuarto carácter (índice 3)
print(texto[:4])

# Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
print(f"{texto:^20[:2]}")

# Formateo a 5 números enteros rellenados con ceros
numero = 150
print(f"{numero:05d}")



#Ejercicio 2
# Leer un archivo de texto
with open("archivo.txt", "r") as archivo:
  contenido = archivo.read()

print(contenido)

# Escribir en un archivo de texto
with open("archivo.txt", "w") as archivo:
  archivo.write("Este es un texto escrito desde el programa Python.")

#Ejercicio 3
import csv

# Leer datos de un archivo CSV
with open("datos.csv", "r") as archivo_csv:
  lector_csv = csv.reader(archivo_csv)
  for fila in lector_csv:
    print(fila)

# Escribir datos en un archivo CSV
with open("datos.csv", "a") as archivo_csv:
  escritor_csv = csv.writer(archivo_csv)
  escritor_csv.writerow(["Nombre", "Apellido", "Edad"])
  escritor_csv.writerow(["Juan", "Pérez", 30])
  escritor_csv.writerow(["María", "Gómez", 25])
