#Leer dos números e imprimir los números entre ellos
def mostrarNumeros(inicio=0, fin=0):
    if(inicio < fin):
        for i in range(inicio, fin+1):
            print(i, end=" ")
    else:
        for i in range(fin, inicio+1):
            print(i, end=" ")

def main():
    inicio = int(input("Ingrese el primer numero: "))
    fin = int(input("Ingrese el segundo numero: "))
    mostrarNumeros(inicio, fin)

main()