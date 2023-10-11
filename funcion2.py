def is_prime(num):
    """Verifica si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(numbers):
    """Devuelve una lista de números primos de una lista de números."""
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# Ejemplo de uso de la función prime_numbers
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros_primos = prime_numbers(lista_numeros)
print(lista_numeros_primos)  # Salida: [2, 3, 5, 7]
