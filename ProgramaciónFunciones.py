#Ejercicio 1
def area_rectangulo(base, altura):
  """
  Función para calcular el área de un rectángulo.

  Argumentos:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

  Retorno:
    float: El área del rectángulo.
  """
  if base <= 0 or altura <= 0:
    raise ValueError("La base y la altura deben ser números positivos.")
  return base * altura

# Ejemplo de uso
base = 15
altura = 10

area_rectangulo = area_rectangulo(base, altura)
print(f"El área del rectángulo de base {base} y altura {altura} es: {area_rectangulo}")

#Ejercicio 2
import math

def area_circulo(radio):
  """
  Función para calcular el área de un círculo.

  Argumentos:
    radio (float): El radio del círculo.

  Retorno:
    float: El área del círculo.
  """
  if radio <= 0:
    raise ValueError("El radio debe ser un número positivo.")
  return math.pi * radio ** 2

# Ejemplo de uso
radio = 5

area_circulo = area_circulo(radio)
print(f"El área del círculo de radio {radio} es: {area_circulo}")

#Ejercicio 3
def relacion(a, b):
  """
  Función para comparar dos números y devolver su relación.

  Argumentos:
    a (float): El primer número.
    b (float): El segundo número.

  Retorno:
    int: 1 si a > b, -1 si a < b, 0 si a == b.
  """
  if a > b:
    return 1
  elif a < b:
    return -1
  else:
    return 0

# Ejemplos de uso
numero1 = 5
numero2 = 10

relacion_numeros = relacion(numero1, numero2)
print(f"La relación entre {numero1} y {numero2} es: {relacion_numeros}")

numero1 = 10
numero2 = 5

relacion_numeros = relacion(numero1, numero2)
print(f"La relación entre {numero1} y {numero2} es: {relacion_numeros}")

numero1 = 5
numero2 = 5

relacion_numeros = relacion(numero1, numero2)
print(f"La relación entre {numero1} y {numero2} es: {relacion_numeros}")

#Ejercicio 4
def intermedio(a, b):
  """
  Función para calcular el punto intermedio entre dos números.

  Argumentos:
    a (float): El primer número.
    b (float): El segundo número.

  Retorno:
    float: El punto intermedio entre a y b.
  """
  return (a + b) / 2

# Ejemplo de uso
numero1 = -12
numero2 = 24

punto_intermedio = intermedio(numero1, numero2)
print(f"El punto intermedio entre {numero1} y {numero2} es: {punto_intermedio}")

#Ejercicio 5
def recortar(numero, minimo, maximo):
  """
  Función para recortar un número dentro de un rango.

  Argumentos:
    numero (float): El número a recortar.
    minimo (float): El límite inferior del rango.
    maximo (float): El límite superior del rango.

  Retorno:
    float: El número recortado, el mínimo o el máximo según corresponda.
  """
  if numero < minimo:
    return minimo
  elif numero > maximo:
    return maximo
  else:
    return numero

# Ejemplo de uso
numero_recortar = 15
limite_minimo = 0
limite_maximo = 10

numero_recortado = recortar(numero_recortar, limite_minimo, limite_maximo)
print(f"El número {numero_recortar} recortado entre {limite_minimo} y {limite_maximo} es: {numero_recortado}")

# Ejemplo adicional con valores fuera del rango
numero_recortar = -5
numero_recortado = recortar(numero_recortar, limite_minimo, limite_maximo)
print(f"El número {numero_recortar} recortado entre {limite_minimo} y {limite_maximo} es: {numero_recortado}")

numero_recortar = 25
numero_recortar = recortar(numero_recortar, limite_minimo, limite_maximo)
print(f"El número {numero_recortar} recortado entre {limite_minimo} y {limite_maximo} es: {numero_recortar}")

#Ejercicio 6
def separar(lista):
  """
  Función para separar pares e impares de una lista de números enteros.

  Argumentos:
    lista (list): La lista de números enteros.

  Retorno:
    tuple: Dos listas, la primera con los pares y la segunda con los impares.
  """
  pares = []
  impares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
    else:
      impares.append(numero)
  return pares, impares

# Ejemplo de uso
lista_numeros = [6, 5, 2, 1, 7, 4, 9]

pares, impares = separar(lista_numeros)
print(f"Lista de pares: {pares}")
print(f"Lista de impares: {impares}")
