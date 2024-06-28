import random
import re

vehiculos = []

def verificar_patente(patente):
    return re.match(r'^[BCDFGHJKLMNPQRSTVWXYZ]{4}\d{2}$', patente) is not None

def verificar_marca(marca):
    return 2 <= len(marca) <= 15

def verificar_precio(precio):
    try:
        precio_sin_puntos = int(precio.replace('.', ''))
        return precio_sin_puntos > 5000000
    except ValueError:
        return False

def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo (Automóvil, Camión, Camioneta, Moto): ")
    
    patente = input("Ingrese la patente (4 letras consonantes y 2 números): ")
    while not verificar_patente(patente):
        print("Patente no válida. Debe ser 4 letras consonantes y 2 números.")
        patente = input("Ingrese la patente: ")
    
    marca = input("Ingrese la marca (entre 2 y 15 caracteres): ")
    while not verificar_marca(marca):
        print("Marca no válida. Debe tener entre 2 y 15 caracteres.")
        marca = input("Ingrese la marca: ")
    
    precio_input = input("Ingrese el precio (mayor a $5.000.000): ")
    while not verificar_precio(precio_input):
        print("Precio no válido. Debe ser mayor a $5.000.000.")
        precio_input = input("Ingrese el precio: ")
    
    multas = []
    num_multas = int(input("Ingrese el número de multas: "))
    for _ in range(num_multas):
        monto = int(input("Ingrese el monto de la multa: "))
        fecha = input("Ingrese la fecha de la multa: ")
        multas.append({'monto': monto, 'fecha': fecha})
    
    fecha_registro = input("Ingrese la fecha de registro: ")
    run = input("Ingrese el RUN del dueño: ")
    nombre_dueño = input("Ingrese el nombre del dueño: ")
    
    vehiculo = {
        'tipo': tipo,
        'patente': patente,
        'marca': marca,
        'precio': int(precio_input.replace('.', '')),
        'multas': multas,
        'fecha_registro': fecha_registro,
        'run': run,
        'nombre_dueño': nombre_dueño
    }
    vehiculos.append(vehiculo)
    print("Vehículo registrado con éxito.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            print(f"Tipo: {vehiculo['tipo']}, Patente: {vehiculo['patente']}, Marca: {vehiculo['marca']}, "
                  f"Precio: ${vehiculo['precio']:,}, Multas: {vehiculo['multas']}, "
                  f"Fecha de registro: {vehiculo['fecha_registro']}, RUN: {vehiculo['run']}, "
                  f"Dueño: {vehiculo['nombre_dueño']}")
            return
    print("Vehículo no encontrado.")

def imprimir_certificados():
    certificados = ["Emisión de contaminantes", "Anotaciones vigentes", "Multas"]
    for vehiculo in vehiculos:
        for certificado in certificados:
            valor = random.randint(1500, 3500)
            print(f"Certificado: {certificado}, Patente: {vehiculo['patente']}, "
                  f"Dueño: {vehiculo['nombre_dueño']}, RUN: {vehiculo['run']}, Valor: ${valor}")

def mostrar_menu():
    print("\nMenú:")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            grabar_vehiculo()
        elif opcion == "2":
            buscar_vehiculo()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
