# Función para verificar si un número es par
def es_par(numero):
    return numero % 2 == 0

# Función para mostrar los números pares hasta un límite
def mostrar_pares(limite):
    contador = 0
    while contador <= limite:
        if es_par(contador):
            print(contador, end=" ")
        contador += 1

# Función principal que solicita el número y llama a mostrar_pares
def main():
    numero = int(input("Ingrese un número positivo: "))
    if numero >= 0:
        print("\nNúmeros pares desde 0 hasta", numero, ":")
        mostrar_pares(numero)
    else:
        print("Debe ingresar un número positivo.")

# Ejecutar el programa
main()
