nombre = input("\nIngrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Error: El precio no puede ser negativo o cero.")
        else:
            break
    except ValueError:
        print("Error: Por favor ingresa un número válido para el precio.")

while True:
    try:
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad <= 0:
            print("Error: El precio no puede ser negativo o cero.")
        else:
            break
    except ValueError:
        print("Error: Por favor ingresa un número válido para el precio.")