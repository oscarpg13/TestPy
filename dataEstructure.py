# EJERCICIO 1
def square_tuple(input_tuple):
  return tuple(x**2 for x in input_tuple)

numbers = (1, 2, 3, 4, 5)
result = square_tuple(numbers)
print(result)  

# EJERCICIO 2
def encontrar_interseccion(conjunto1, conjunto2):
    """Encuentra la intersección de dos conjuntos."""
    return conjunto1.intersection(conjunto2)

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

resultado = encontrar_interseccion(conjunto1, conjunto2)
print("Intersección de los conjuntos:", resultado)

# EJERCICIO 3
def fusionar_diccionarios(diccionario1, diccionario2):
    """Fusiona dos diccionarios y utiliza los valores del segundo diccionario en caso de claves comunes."""
    diccionario1.update(diccionario2)
    return diccionario1

# Ejemplo de uso
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'c': 5, 'd': 6}

resultado = fusionar_diccionarios(diccionario1, diccionario2)
print("Diccionario fusionado:", resultado)

# EJERCICIO 4
def crear_diccionario_longitudes(words):
    """Crea un diccionario donde las claves son las cadenas y los valores son las longitudes de las cadenas."""
    return {cadena: len(cadena) for cadena in words}

# Ejemplo de uso
words = ["apple", "banana", "cherry"]
diccionario_longitudes = crear_diccionario_longitudes(words)
print("Diccionario de longitudes:", diccionario_longitudes)
