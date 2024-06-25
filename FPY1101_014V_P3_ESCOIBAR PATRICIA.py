import random
import re

class Vehiculo:
    def __init__(self, tipo, patente, marca, precio, multas, fecha_registro, run, nombre_dueño):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.multas = multas
        self.fecha_registro = fecha_registro
        self.run = run
        self.nombre_dueño = nombre_dueño

    def __str__(self):
        return (f"Tipo: {self.tipo}, Patente: {self.patente}, Marca: {self.marca}, Precio: ${self.precio:,}, "
                f"Multas: {self.multas}, Fecha de registro: {self.fecha_registro}, RUN: {self.run}, Dueño: {self.nombre_dueño}")

vehiculos = []

def verificar_patente(patente):
    return re.match(r'^[BCDFGHJKLMNPQRSTVWXYZ]{4}\d{2}$', patente) is not None

def verificar_marca(marca):
    return 2 <= len(marca) <= 15

def verificar_precio(precio):
    try:
        # Eliminar puntos de miles y convertir a entero
        precio_sin_puntos = int(precio.replace('.', ''))
        return precio_sin_puntos > 5000000
    except ValueError:
        return False

def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo (Automóvil, Camión, Camioneta, Moto): ")
    
    # Verificar patente
    patente = input("Ingrese la patente del vehículo (4 letras consonantes y 2 números): ")
    while not verificar_patente(patente):
        print("Patente no válida. Debe ser 4 letras consonantes (excepto M, N, Ñ), seguido por 2 números.")
        patente = input("Ingrese la patente del vehículo (4 letras consonantes y 2 números): ")
    
    # Verificar marca
    marca = input("Ingrese la marca del vehículo (entre 2 y 15 caracteres): ")
    while not verificar_marca(marca):
        print("Marca no válida. Debe tener entre 2 y 15 caracteres.")
        marca = input("Ingrese la marca del vehículo (entre 2 y 15 caracteres): ")
    
    # Verificar precio
    precio_input = input("Ingrese el precio del vehículo (mayor a $5.000.000): ")
    while True:
        try:
            if verificar_precio(precio_input):
                break
            else:
                print("Precio no válido. Debe ser mayor a $5.000.000.")
        except ValueError:
            print("Formato de precio no válido. Ingrese el precio como un número sin puntos ni comas.")
        precio_input = input("Ingrese el precio del vehículo (mayor a $5.000.000): ")
    
    # Ingresar multas
    multas = []
    num_multas = int(input("Ingrese el número de multas: "))
    for _ in range(num_multas):
        monto = int(input("Ingrese el monto de la multa: "))
        fecha = input("Ingrese la fecha de la multa: ")
        multas.append({'monto': monto, 'fecha': fecha})
    
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    run = input("Ingrese el RUN del dueño: ")
    nombre_dueño = input("Ingrese el nombre del dueño: ")
    
    # Crear y agregar el vehículo
    vehiculo = Vehiculo(tipo, patente, marca, int(precio_input.replace('.', '')), multas, fecha_registro, run, nombre_dueño)
    vehiculos.append(vehiculo)
    print("Vehículo registrado con éxito.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    for vehiculo in vehiculos:
        if vehiculo.patente == patente:
            print(vehiculo)
            return
    print("Vehículo no encontrado.")

def imprimir_certificados():
    certificados = ["Emisión de contaminantes", "Anotaciones vigentes", "Multas"]
    for vehiculo in vehiculos:
        for certificado in certificados:
            valor = random.randint(1500, 3500)
            print(f"Certificado: {certificado}, Patente: {vehiculo.patente}, Dueño: {vehiculo.nombre_dueño}, RUN: {vehiculo.run}, Valor: ${valor}")

def mostrar_menu():
    print("\nMenú:")
    print("1. Grabar")
    print("2. Buscar")
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
            print("Programa desarrollado por Patricia Escobar, versión 1.0")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
