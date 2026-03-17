inventario = []

while True:
    print("")
    print("--" * 9)
    print("       Menú       ")
    print("--" * 9)
    print("\n1. Agregar producto")
    print("\n2. Mostrar inventario")
    print("\n3. Calcular estadistica")
    print("\n4. Salir")

    try:
        opcion = int(input("\nQue opción deseas realizar: "))
        
        if opcion == 1:
            nombre = input("\nIngresa el nombre del producto: ")
            precio = float(input("\nIngresa el precio del producto: "))
            cantidad = int(input("\nIngresa la cantidad del producto: "))
            producto = {
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad
            }

            inventario.append(producto)
            print("\nProducto agregado correctamente.")

        elif opcion == 2:
            if len(inventario) == 0:
                print("\nEl inventario esta vacio.")
            else:
                print("----------------Inventario ----------------")
                for producto in inventario:
                    print(f"\nProducto: {producto['Nombre']} | Precio: {producto['Precio']} | Cantidad: {producto['Cantidad']}")

        elif opcion == 3:
            total = 0
            cantidad_total = 0
            for producto in inventario:
                total += producto["Precio"] * producto["Cantidad"]
                cantidad_total += producto["Cantidad"]
                print(f"\nValor total del inventario: {total}")
                print(f"\nCantidad total del producto: {cantidad_total}")

        elif opcion == 4:
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpcion invalida")
    except ValueError:
        print("\nIngresa ingresa datos validos.")