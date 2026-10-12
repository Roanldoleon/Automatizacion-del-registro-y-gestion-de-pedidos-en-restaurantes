# Sistema de pedidos de un restaurante pequeño
# Version 3 : validacion del pedido, pago, vuelto y estado

# ENTRADA

def ingresarPedido(productosDisponibles, preciosDisponibles):

    productos = []
    cantidades = []
    precios = []

    cliente = input("Nombre del cliente: ")
    mesa = int(input("Numero de mesa: "))

    for i in range(0, len(productosDisponibles), 1):
        print(i + 1, productosDisponibles[i], "S/.", preciosDisponibles[i])

    continuar = "S"

    while continuar == "S":

        opcion = int(input("Seleccione un producto (1-4): "))
        cantidad = int(input("Cantidad: "))

        if opcion >= 1 and opcion <= len(productosDisponibles) and cantidad > 0:
            productos.append(productosDisponibles[opcion - 1])
            precios.append(preciosDisponibles[opcion - 1])
            cantidades.append(cantidad)
        else:
            print("Datos incorrectos")

        continuar = input("Agregar otro producto? (S/N): ").upper()

    return cliente, mesa, productos, cantidades, precios


# PROCESO

def obtenerTotal(precios, cantidades):

    total = 0

    for i in range(0, len(precios), 1):
        total += precios[i] * cantidades[i]

    return total


def procesarPago(total):

    pago = float(input("Monto recibido: S/. "))

    while pago < total:
        print("Pago insuficiente")
        pago = float(input("Ingrese nuevamente el monto recibido: "))

    vuelto = pago - total

    return vuelto


# SALIDA

def mostrarPedido(cliente, mesa, productos, cantidades, total, vuelto):

    print("\n----- RESUMEN DEL PEDIDO -----")
    print("Cliente:", cliente)
    print("Mesa:", mesa)

    for i in range(0, len(productos), 1):
        print(productos[i], "Cantidad:", cantidades[i])

    print("Total a pagar: S/.", format(total, ".2f"))
    print("Pago correcto. Vuelto: S/.", format(vuelto, ".2f"))
    print("Estado del pedido: Listo para entregar")


# PROGRAMA PRINCIPAL

def pedidos():

    productosDisponibles = ["Arroz chaufa", "Caldo de gallina", "Aji de pollo", "Chicha morada"]
    preciosDisponibles = [12, 15, 10, 5]

    cliente, mesa, productos, cantidades, precios = ingresarPedido(productosDisponibles, preciosDisponibles)

    if cliente != "" and mesa > 0 and len(productos) > 0:

        total = obtenerTotal(precios, cantidades)

        print("Total a pagar: S/.", total)

        vuelto = procesarPago(total)

        mostrarPedido(cliente, mesa, productos, cantidades, total, vuelto)

    else:
        print("No se puede registrar el pedido")


pedidos()


pedidos()



