#Leer dos números e imprimir los números entre ellos
def mostrarNumeros(inicio=0, fin=0):
    if(inicio < fin):
        for num in range(inicio, fin+1):
            print(i, end=" ")
    else:
        num=inicio
        while(num>=fin):
            print(num)
            num-= 1

inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))
mostrarNumeros(inicio, fin)
