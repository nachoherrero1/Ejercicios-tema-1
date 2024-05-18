#Ejercicio 1
usuarios = set(["Marta", "David", "Elvira", "Juan", "Marcos"])
administradores = set(["Juan", "Marta"])

# Borrar a Juan de administradores
administradores.remove("Juan")

# Añadir a Marcos como administrador
administradores.add("Marcos")

# Recorrer usuarios y mostrar si son administradores
print("Usuarios:")
for usuario in usuarios:
  if usuario in administradores:
    print(f"- {usuario} (administrador)")
  else:
    print(f"- {usuario}")

#Ejercicio 2
class Personaje:
  def __init__(self, nombre, vida_base, defensa_base, ataque_base, alcance_base):
    self.nombre = nombre
    self.vida = vida_base
    self.defensa = defensa_base
    self.ataque = ataque_base
    self.alcance = alcance_base

caballero = Personaje("Caballero", 200, 400, 100, 2)
guerrero = Personaje("Guerrero", 100, 200, 200, 4)
arquero = Personaje("Arquero", 100, 100, 200, 6)

# Ajustar propiedades según la clase
caballero.vida *= 2
caballero.defensa *= 2
guerrero.ataque *= 2
guerrero.alcance *= 2
arquero.ataque = guerrero.ataque
arquero.defensa = guerrero.defensa / 2
arquero.alcance *= 2

# Mostrar propiedades de cada personaje
print("Caballero:")
print(f"- Vida: {caballero.vida}")
print(f"- Defensa: {caballero.defensa}")
print(f"- Ataque: {caballero.ataque}")
print(f"- Alcance: {caballero.alcance}")

print("\nGuerrero:")
print(f"- Vida: {guerrero.vida}")
print(f"- Defensa: {guerrero.defensa}")
print(f"- Ataque: {guerrero.ataque}")
print(f"- Alcance: {guerrero.alcance}")

print("\nArquero:")
print(f"- Vida: {arquero.vida}")
print(f"- Defensa: {arquero.defensa}")
print(f"- Ataque: {arquero.ataque}")
print(f"- Alcance: {arquero.alcance}")

#Ejercicio 3
import heapq

class Tarea:
  def __init__(self, nombre, prioridad):
    self.nombre = nombre
    self.prioridad = prioridad

# Creamos la cola de tareas
cola_tareas = []

# Añadimos las tareas con su nombre y prioridad (menor número, mayor prioridad)
heapq.heappush(cola_tareas, Tarea("Limpiar casa", 1))
heapq.heappush(cola_tareas, Tarea("Estudiar examen", 2))
heapq.heappush(cola_tareas, Tarea("Hacer compra", 3))
heapq.heappush(cola_tareas, Tarea("Ir al gimnasio", 4))

# Mostramos la próxima tarea a realizar (la de mayor prioridad)
while cola_tareas:
  tarea = heapq.heappop(cola_tareas)
  print(f"Siguiente tarea: {tarea.nombre} (Prioridad: {tarea.prioridad})")
