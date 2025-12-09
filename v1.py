# Sistema de Analisis de Endeudamiento - RokoBank

print("=== Sistema de Evaluación de Endeudamiento - RokoBank ===")

dni = input("Ingrese el DNI del solicitante: ")

num_deudas = int(input("¿Cuántas deudas tiene el cliente?: "))
while num_deudas < 0:
    print("El número de deudas no puede ser negativo.")
    num_deudas = int(input("¿Cuántas deudas tiene el cliente?: "))

deudas = []

for i in range(num_deudas):
    monto = float(input(f"Ingrese el monto de la deuda {i+1}: "))
    while monto < 0:
        print("El monto no puede ser negativo.")
        monto = float(input(f"Ingrese nuevamente el monto de la deuda {i+1}: "))
    deudas.append(monto)

ingresos = float(input("Ingrese los ingresos mensuales del cliente: "))
while ingresos < 0:
    print("Los ingresos no pueden ser negativos.")
    ingresos = float(input("Ingrese nuevamente los ingresos mensuales: "))

print("Datos registrados correctamente.")
