# Ejercicio 1: Escribir una función que tome una lista de números como argumento y devuelva la suma de los números impares en la lista.
def suma_impares(numeros):
    """Sumar los números impares en una lista de números y devolver el resultado."""
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

# Ejercicio 2: Escribir una función que tome una lista de números y devuelva una nueva lista con elementos únicos de la primera lista.
def elementos_unicos(numeros):
    """Devolver una lista de elementos únicos de una lista."""
    unicos = list(set(numeros))
    return unicos

# Ejercicio 3: Escribir una función que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista, en el mismo orden.
def lista_unicos_ordenada(numeros):
    """Devolver una lista de elementos únicos de una lista, en el orden de la lista original."""
    unicos = []
    for num in numeros:
        if num not in unicos:
            unicos.append(num)
    return unicos

# Ejercicio 4: Escribir una función que tome una lista de números y devuelva una nueva lista con solo los números pares de la primera lista.
def numeros_pares(numeros):
    """Devolver una lista de números pares de una lista de números."""
    pares = [num for num in numeros if num % 2 == 0]
    return pares

# Ejercicio 5: Escribir una función que tome una lista de números y devuelva una nueva lista con solo los números impares de la primera lista.
def numeros_impares(numeros):
    """Devolver una lista de números impares de una lista de números."""
    impares = [num for num in numeros if num % 2 != 0]
    return impares

# Ejercicio 6: Escribir una función que tome una lista de números y devuelva una nueva lista con solo los números primos de la primera lista.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(numeros):
    """Devolver una lista de números primos de una lista de números."""
    primos = [num for num in numeros if es_primo(num)]
    return primos

# Ejercicio 7: Escribir una función que tome una lista de números y devuelva una nueva lista con solo los palíndromos de la primera lista.
def es_palindromo(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def numeros_palindromos(numeros):
    """Devolver una lista de números palíndromos de una lista de números."""
    palindromos = [num for num in numeros if es_palindromo(num)]
    return palindromos

# Lista de números de muestra
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Utilizando las funciones
# Ejercicio 1
suma_de_impares = suma_impares(numeros)
print("Ejercicio 1: Suma de números impares:", suma_de_impares)

# Ejercicio 2
elementos_unicos = elementos_unicos(numeros)
print("Ejercicio 2: Elementos únicos:", elementos_unicos)

# Ejercicio 3
unicos_ordenados = lista_unicos_ordenada(numeros)
print("Ejercicio 3: Elementos únicos en el mismo orden:", unicos_ordenados)

# Ejercicio 4
numeros_pares_resultado = numeros_pares(numeros)
print("Ejercicio 4: Números pares:", numeros_pares_resultado)

# Ejercicio 5
numeros_impares_resultado = numeros_impares(numeros)
print("Ejercicio 5: Números impares:", numeros_impares_resultado)

# Ejercicio 6
numeros_primos_resultado = numeros_primos(numeros)
print("Ejercicio 6: Números primos:", numeros_primos_resultado)

# Ejercicio 7
numeros2 = [121, 12321, 123, 456, 78987]
palindromos_resultado = numeros_palindromos(numeros2)
print("Ejercicio 7: Palíndromos:", palindromos_resultado)