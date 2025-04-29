#Leer un número ingresado por el usuario
#Mostrar la letra "A" por cada numero del 1 al ingresado
#Ej: Número: 3
#a
#aa
#aaa

def mostrarLetra(numero):
    for i in range(numero+1):
        print(f"a"*i)

def main():
    num = int(input("Ingrese un número: "))
    mostrarLetra(num)

main()