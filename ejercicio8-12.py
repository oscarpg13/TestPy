numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("MENU:")
    print("1. Imprimir los primeros cinco elementos")
    print("2. Imprimir números pares")
    print("3. Imprimir números impares")
    print("4. Imprimir múltiplos de 5")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        print(numList[:5])
    elif opcion == "2":
        print("Números pares:")
        print(numList[1::2])
    elif opcion == "3":
        print("Números impares:")
        print(numList[::2])
    elif opcion == "4":
        print("Múltiplos de 5:")
        print(numList[4::5])
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
