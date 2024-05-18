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

# Ejemplo de uso (con error)
try:
  base = -5
  altura = 10

  area_rectangulo = area_rectangulo(base, altura)
  print(f"El área del rectángulo de base {base} y altura {altura} es: {area_rectangulo}")
except ValueError as error:
  print(f"Error: {error}")

# Ejemplo de uso (sin error)
base = 15
altura = 10

area_rectangulo = area_rectangulo(base, altura)
print(f"El área del rectángulo de base {base} y altura {altura} es: {area_rectangulo}")

#Ejercicio 2
def obtener_elemento(lista, indice):
  """
  Función para obtener un elemento de una lista por su índice.

  Argumentos:
    lista (list): La lista de elementos.
    indice (int): El índice del elemento a obtener.

  Retorno:
    any: El elemento de la lista en la posición indicada por el índice o `None` si hay un error.
  """
  try:
    return lista[indice]
  except IndexError as error:
    print(f"Error: {error}")
    return None

# Ejemplo de uso adicional (con error de tipo `TypeError`)
indice = "cinco"

elemento = obtener_elemento([1, 2, 3, 4, 5], indice)
print(f"El elemento en la posición {indice} es: {elemento}")

# Ejericio 3
def obtener_valor_diccionario(diccionario, clave):
  """
  Función para obtener un valor de un diccionario por su clave.

  Argumentos:
    diccionario (dict): El diccionario de datos.
    clave (str): La clave del valor a obtener.

  Retorno:
    any: El valor asociado a la clave especificada o `None` si hay un error.
  """
  try:
    return diccionario[clave]
  except KeyError as error:
    print(f"Error: {error}")
    return None

# Ejemplo de uso (con error)
clave = "color"

valor = obtener_valor_diccionario({"nombre": "Juan", "edad": 30}, clave)
print(f"El valor de la clave '{clave}' es: {valor}")

# Ejemplo de uso (sin error)
clave = "nombre"

valor = obtener_valor_diccionario({"nombre": "Juan", "edad": 30}, clave)
print(f"El valor de la clave '{clave}' es: {valor}")

#Ejercicio 4
def sumar(valor1, valor2):
  """
  Función para sumar dos valores.

  Argumentos:
    valor1 (any): El primer valor a sumar.
    valor2 (any): El segundo valor a sumar.

  Retorno:
    any: La suma de los dos valores o un mensaje de error si no son compatibles.
  """
  try:
    return valor1 + valor2
  except TypeError as error:
    print(f"Error: {error}")
    return f"No se pueden sumar tipos incompatibles: {type(valor1)} y {type(valor2)}"

# Ejemplos de uso (con y sin errores)
valor1 = 10
valor2 = 5

resultado = sumar(valor1, valor2)
print(f"Suma de {valor1} y {valor2}: {resultado}")

valor1 = "Hola"
valor2 = 2

resultado = sumar(valor1, valor2)
print(f"Suma de {valor1} y {valor2}: {resultado}")

valor1 = [1, 2, 3]
valor2 = 4

resultado = sumar(valor1, valor2)
print(f"Suma de {valor1} y {valor2}: {resultado}")

#Ejercicio 5
def agregar_una_vez(lista, elemento):
  """
  Función para agregar un elemento a una lista sin duplicados.

  Argumentos:
    lista (list): La lista a la que se desea agregar el elemento.
    elemento (any): El elemento a agregar.

  Retorno:
    None: Si se agrega el elemento correctamente.
    ValueError: Si el elemento ya existe en la lista.
  """
  if elemento in lista:
    raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}")
  lista.append(elemento)

# Ejemplo de uso (sin error)
elementos = [10, -2, "Hola"]

agregar_una_vez(elementos, "Mundo")
print(f"Lista actualizada: {elementos}")

# Ejemplo de uso (con error)
agregar_una_vez(elementos, "Hola")

