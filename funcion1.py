def even_numbers(numbers):
    """Return a list of even numbers from a list of numbers."""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = even_numbers(num)
print(pares)  
