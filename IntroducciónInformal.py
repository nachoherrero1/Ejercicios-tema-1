#Ejercicio 2
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]

print(a * 5)  # 50
print(a - b)  # 15
print(c + "Mundo")  # Hola Mundo
print(c * 2)  # Hola Hola
print(d[-1])  # 3
print(d[1:])  # [2, 3]
print(d + d)  # [1, 2, 3, 1, 2, 3]

#Ejercicio 3
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3  # Se ha corregido la división entera (/) por una división flotante (/)
print("La nota media es", media)  # 6.0

#Ejercicio 4
nota_1 = 10
nota_2 = 7
nota_3 = 4

porcentaje_1 = 15 / 100
porcentaje_2 = 35 / 100
porcentaje_3 = 50 / 100

nota_final = (nota_1 * porcentaje_1) + (nota_2 * porcentaje_2) + (nota_3 * porcentaje_3)

print("La nota final es", nota_final)  # 7.25

#ejercicio 5
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

for fila in matriz:
    fila[-1] = sum(fila[:-1])  # Se utiliza slicing para obtener los elementos hasta el último (excluido)

print(matriz)

#Ejercicio 6
cadena = "zeréP nauJ,01"

# Invertir la cadena
cadena_invertida = cadena[::-1]

# Separar nombre y nota
nombre_apellido, nota = cadena_invertida.split(",")

# Formatear la salida
resultado = f"{nombre_apellido} ha sacado un {nota} de nota."

print(resultado)  # Juan Pérez ha sacado un 1 de nota.
