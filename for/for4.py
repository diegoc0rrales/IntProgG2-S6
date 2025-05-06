numero = int(input("Ingresa un número para calcular sus tablas de multiplicar: "))
print(f"Tablas de multiplicar del {numero}: ")

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
