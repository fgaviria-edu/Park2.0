from datetime import datetime

# Lista vacía
parqueadero = []

# Capacidad
capacidad_carros = 3
capacidad_motos = 2

# Menú
def mostrar_menu():
    print("\n--- Parqueadero ---")
    print("1. Ingreso Carro")
    print("2. Ingreso Moto")
    print("3. Retiro Carro")
    print("4. Retiro Moto")
    print("5. Listado de vehículos en el parqueadero")
    print("6. Salir")

def ingreso_carro():
    if len([v for v in parqueadero if v["tipo"] == "carro"]) >= capacidad_carros:
        print("No hay cupo para carros.")
        return
    registrar_vehiculo("carro")

def ingreso_moto():
    if len([v for v in parqueadero if v["tipo"] == "moto"]) >= capacidad_motos:
        print("No hay cupo para motos.")
        return
    registrar_vehiculo("moto")

def registrar_vehiculo(tipo_predeterminado=None):
    placa = input("Ingrese la placa del vehículo entrante: ").strip().upper()
    if any(v["placa"] == placa for v in parqueadero):
        print("El vehículo ya está en el parqueadero.")
        return

    tipo = tipo_predeterminado
    hora_ingreso = datetime.now()
    vehiculo = {"placa": placa, "tipo": tipo, "hora_ingreso": hora_ingreso}
    parqueadero.append(vehiculo)
    print("Vehículo ingresó correctamente.")

def retiro_carro():
    retiro_vehiculo("carro")

def retiro_moto():
    retiro_vehiculo("moto")

def retiro_vehiculo(tipo):
    placa = input(f"Ingrese la placa del {tipo} saliente: ").strip().upper()
    for i, vehiculo in enumerate(parqueadero):
        if vehiculo["placa"] == placa and vehiculo["tipo"] == tipo:
            hora_salida = datetime.now()
            hora_ingreso = vehiculo["hora_ingreso"]
            tiempo_estacionado = hora_salida - hora_ingreso
            tarifa = 5000 if tipo == "carro" else 1000
            print(f"Tiempo estacionado: {tiempo_estacionado}, Tarifa a pagar: {tarifa} pesos.")
            parqueadero.pop(i)
            print(f"{tipo.capitalize()} salió correctamente.")
            return
    print(f"{tipo.capitalize()} no encontrado o no coincide con el tipo.")

def listar_vehiculos():
    if not parqueadero:
        print("No hay vehículos en el parqueadero.")
        return
    print("\nVehículos en el parqueadero:")
    for v in parqueadero:
        print(f"Placa: {v['placa']}, Tipo: {v['tipo']}, Hora Ingreso: {v['hora_ingreso']}")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ingreso_carro()
    elif opcion == "2":
        ingreso_moto()
    elif opcion == "3":
        retiro_carro()
    elif opcion == "4":
        retiro_moto()
    elif opcion == "5":
        listar_vehiculos()
    elif opcion == "6":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.")

