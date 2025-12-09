# Sistema de Análisis de Endeudamiento - RokoBank

print("=== Sistema de Evaluación de Endeudamiento - RokoBank ===")


dni = input("Ingrese el DNI del solicitante: ")


num_deudas = int(input("¿Cuántas deudas tiene el cliente?: "))
while num_deudas < 0:
    print("El número de deudas no puede ser negativo.")
    num_deudas = int(input("¿Cuántas deudas tiene el cliente?: "))


deudas = []


for i in range(num_deudas):
    print(f"Ingrese el monto de la deuda {i+1}: ")
    monto = float(input())
    
    while monto < 0:
        print("El monto no puede ser negativo. Intente de nuevo.")
        monto = float(input("Ingrese nuevamente el monto de la deuda: "))
    
    deudas.append(monto)


ingresos = float(input("Ingrese los ingresos mensuales del cliente: "))
while ingresos < 0:
    print("Los ingresos no pueden ser negativos.")
    ingresos = float(input("Ingrese nuevamente los ingresos mensuales: "))


total_deuda = 0
for d in deudas:
    total_deuda += d


if ingresos == 0:
    ratio = "Indefinido (no se puede dividir entre 0)"
else:
    ratio = total_deuda / ingresos


if ingresos == 0:
    riesgo = "No calculable"
else:
    if ratio <= 0.30:
        riesgo = "Riesgo Bajo"
    elif ratio <= 0.50:
        riesgo = "Riesgo Moderado"
    else:
        riesgo = "Riesgo Alto"

print("\n=== RESULTADOS ===")
print("DNI del cliente:", dni)
print("Deudas registradas:", deudas)
print("Total de deuda: S/", total_deuda)

if ingresos == 0:
    print("Ratio de endeudamiento: Indefinido")
else:
    print("Ratio de endeudamiento:", round(ratio, 2))

print("Clasificación del riesgo:", riesgo)
