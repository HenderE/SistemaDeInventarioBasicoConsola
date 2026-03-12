#Presentacion del programa
print("")
print("------ Registro de inventario ------")
print("")

# --- Captura de datos del usuario ---
nombre = input("\nIngrese el nombre del producto: ")

# --- Validación del Precio ---
while True:
    try:
        precio = float(input("\nIngrese el precio del producto: "))
        if precio <= 0:
            print("\nError: El precio no puede ser negativo o cero.")
        else:
            break
    except ValueError:
        print("\nError: Por favor ingresa un número válido para el precio.")

# --- Validación de la Cantidad ---
while True:
    try:
        cantidad = int(input("\nIngresa la cantidad: "))
        if cantidad <= 0:
            print("\nError: El precio no puede ser negativo o cero.")
        else:
            break
    except ValueError:
        print("\nError: Por favor ingresa un número válido para el precio.")


# --- Cálculos y Procesamiento ---
# Calculamos el valor total multiplicando precio por unidades
costo_total = precio * cantidad

#Salida de resultados
print(f"\nNombre del producto: {nombre} || Precio: {precio} || Cantidad: {cantidad} || Total: {costo_total}")
