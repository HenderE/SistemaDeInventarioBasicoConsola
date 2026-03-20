 #creo el menú para mostrar al usuario.
def menu():
            print("")
            print("--" * 8)
            print("     Menú     ")
            print("--" * 8)
            #muestro las opciones disponibles.
            print("\n1. Agregar producto")
            print("\n2. Mostrar producto")
            print("\n3. Calcular estadisticas")
            print("\n4. Salir")

#creo funcion para agregar producto y luego llamar la funcion en su respectiva opcion 
def agregar_producto():
            #pido los datos del producto mediante una funcion
            nombre = input("\nIngrese nombre del producto: ")
            precio = float(input("\nIngrese el precio del producto: "))
            cantidad = int(input("\nIngrese la cantidad del producto: "))
            producto = {
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad
            }
            #agrego el producto pedido
            inventario.append(producto)
            print("\nProducto agregado correctamente.")
#creo funcion para mostrar producto y luego llamar la funcion en su respectiva opcion para mostrar al usuario
def mostrar_producto():
            #verifico si el inventario esta vacio
            if len(inventario) == 0:
                print("")
                print("\nInventario Vacio.")
            else:
                print("")
                print("------------------ Inventario ------------------")
                #recorro la lista y muestro cada producto
                for producto in inventario:
                    print(f"\nProducto: {producto['Nombre']} | Precio: {producto['Precio']} | Cantidad: {producto['Cantidad']}")
#creo funcion para calcular el producto y luego llamar la funcion en su respectiva opcion
def calcular_producto():
            #hacemos el calculo de las estadisticas del inventario
            total = 0
            cantidad_total = 0
            #recorro el inventario para calcular el valor total y cantidad total
            for producto in inventario:
                total += producto["Precio"] * producto["Cantidad"]
                cantidad_total += producto["Cantidad"]
            #muestro los resultados
            print(f"\nValor total del inventario: {total}")
            print(f"\nCantidad total de productos: {cantidad_total}")

#creo una variale llamada inventario donde guardo varios productos
#cada producto es un diccionario con su nombre, precio y cantidad
inventario = [
    {"Nombre": "Cilantro", "Precio": 1000, "Cantidad": 5},
    {"Nombre": "Pera", "Precio": 2500, "Cantidad": 6},
    {"Nombre": "Manzana", "Precio": 1500, "Cantidad": 4},
    {"Nombre": "Doritos", "Precio": 8000, "Cantidad": 2},
    {"Nombre": "Harina Pan", "Precio": 5000, "Cantidad": 1}
    ]

#uso un ciclo infinito para que el menú se repita hasta que el usuario decida salirse. 
while True:
    #muestro el menu mediante funcion
    menu()
    try:
        #le pido al usuario que ingrese una opción
        opcion = int(input("\nIngrese una opción: "))
        
        #opciones disponibles
        if opcion == 1:
            agregar_producto()
        
        elif opcion == 2:
            
            mostrar_producto()
        
        elif opcion == 3:
            calcular_producto()

        #opcion4: salir del programa
        elif opcion == 4:
            print("\nSaliendo del sistema...")
            break
        else:
            #si el usuario ingresa una opcion que no existe
            print("\nOpcion Invalida.")
    except ValueError:
        #manejanmos el error si el usuario no ingresa un numero valido
        print("\nIngresa un dato valido.")


    #----------------------------------------Comentario Final----------------------------------------
    """El objetivo de esta semana era realizar el feature 2 de la epic en la cual estamos trabajando.
    registramos valores como nombre, precio y cantidad, trabajamos con listas, diccionarios dentro de
    una lista y tambien trabajamos dentro de un ciclo infinito con opcion para salir del programa.
    creamos un inventario el cual agrega producto, visualiza el producto y calcula las estadisticas del
    inventario mostrandoselas al cliente."""