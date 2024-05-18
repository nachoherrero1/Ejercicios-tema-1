#Ejercicio 1
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print("Los dos números son iguales") if numero1 == numero2 else None
print("Los dos números son diferentes") if numero1 != numero2 else None
print("El primer número es mayor que el segundo") if numero1 > numero2 else None
print("El segundo número es mayor o igual que el primero") if numero2 >= numero1 else None

#Ejercicio 2
cadena = input("Introduce una cadena de texto: ")

if len(cadena) >= 3 and len(cadena) < 10:
    print("La cadena cumple la condición")
else:
    print("La cadena no cumple la condición")

#Ejercicio 3
numero_magico = 12345679
numero_usuario = int(input("Introduce un número entre 1 y 9: "))

numero_usuario_cuadrado = numero_usuario * numero_usuario
numero_magico_cuadrado = numero_magico * numero_usuario * numero_usuario

numero_magico *= numero_usuario_cuadrado

print("El valor final de 'numero_magico' es:", numero_magico)

#Ejercicio 4
def suma(numero1, numero2):
  return numero1 + numero2

def resta(numero1, numero2):
  return numero1 - numero2

def multiplicacion(numero1, numero2):
  return numero1 * numero2

while True:
  try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    opcion = int(input("""
    Elige una opción:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Salir
    Opción: """))

    if opcion == 1:
      resultado = suma(numero1, numero2)
      print(f"La suma de {numero1} y {numero2} es: {resultado}")
    elif opcion == 2:
      resultado = resta(numero1, numero2)
      print(f"La resta de {numero1} y {numero2} es: {resultado}")
    elif opcion == 3:
      resultado = multiplicacion(numero1, numero2)
      print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
    elif opcion == 4:
      print("Saliendo del programa...")
      break
    else:
      print("Opción no válida. Inténtalo de nuevo.")

  except ValueError:
    print("Error: Debes introducir números válidos.")

#Ejercicio 5
while True:
  try:
    numero = int(input("Introduce un número impar: "))
    if numero % 2 != 0:
      print(f"¡Has introducido un número impar! El número es: {numero}")
      break
    else:
      print("El número introducido no es impar. Inténtalo de nuevo.")
  except ValueError:
    print("Error: Debes introducir un número entero.")

#Ejercicio 6
suma_pares = 0

for numero in range(0, 101, 2):
  suma_pares += numero

print("La suma de los números pares entre 0 y 100 es:", suma_pares)

#Ejercicio 7
cantidad_numeros = int(input("¿Cuántos números quieres introducir?: "))
suma_numeros = 0

for i in range(cantidad_numeros):
  try:
    numero = float(input(f"Introduce el número {i + 1}: "))
    suma_numeros += numero
  except ValueError:
    print("Error: Debes introducir un número válido.")

if suma_numeros != 0:
  media = suma_numeros / cantidad_numeros
  print(f"La media de los números introducidos es: {media}")
else:
  print("No se han introducido números válidos.")

#Ejercicio 8
lista_numeros = [1, 5, 7, 12, 14, 18, 23, 25, 31, 37]

numero_objetivo = int(input("Introduce un número para buscar: "))

if numero_objetivo in lista_numeros:
  print(f"El número {numero_objetivo} sí se encuentra en la lista.")
else:
  print(f"El número {numero_objetivo} no se encuentra en la lista.")

#Ejercicio 9
def generar_lista(inicio, fin, salto=1):
  """
  Genera una lista dinámicamente utilizando range.

  Argumentos:
    inicio (int): Valor inicial del rango.
    fin (int): Valor final del rango.
    salto (int, opcional): Salto del rango (por defecto 1).

  Retorno:
    list: Lista generada con los valores del rango.
  """
  return list(range(inicio, fin, salto))

# Ejemplo de uso
lista_del_0_al_10 = generar_lista(0, 11)  # Lista del 0 al 10 (incluido el 10)
lista_negativos_del_10_al_0 = generar_lista(-10, 1, -1)  # Lista del -10 al 0 (de -1 en -1)
lista_pares_del_0_al_20 = generar_lista(0, 21, 2)  # Lista de pares del 0 al 20 (incluido el 20)
lista_impares_entre_neg20_y_0 = generar_lista(-20, 1, -2)  # Lista de impares entre -20 y 0 (de -2 en -2)
lista_multiples_de_5_del_0_al_50 = generar_lista(0, 51, 5)  # Lista de múltiplos de 5 del 0 al 50 (incluido el 50)

print(lista_del_0_al_10)
print(lista_negativos_del_10_al_0)
print(lista_pares_del_0_al_20)
print(lista_impares_entre_neg20_y_0)
print(lista_multiples_de_5_del_0_al_50)

#Ejercicio 10
lista_1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista_2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

elementos_repetidos = set(lista_1) & set(lista_2)

print("Elementos repetidos en ambas listas:", elementos_repetidos)


#Ejercicio 11
from collections import deque

# Definimos la cola de tareas
cola_tareas = deque()

# Añadimos las tareas con su orden de prioridad
cola_tareas.append(("Limpiar casa", 1))
cola_tareas.append(("Estudiar examen", 2))
cola_tareas.append(("Hacer compra", 3))
cola_tareas.append(("Ir al gimnasio", 4))

# Mostramos las tareas sin orden
print("Tareas sin ordenar:")
for tarea, prioridad in cola_tareas:
  print(f"- {tarea} (Prioridad: {prioridad})")

# Ordenamos la cola por prioridad (ascendente)
cola_tareas.sort(key=lambda tarea: tarea[1])

# Mostramos las tareas ordenadas
print("\nTareas ordenadas por prioridad:")
for tarea, prioridad in cola_tareas:
  print(f"- {tarea} (Prioridad: {prioridad})")
