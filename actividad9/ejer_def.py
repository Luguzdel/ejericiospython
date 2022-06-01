#Punto a y b

from audioop import reverse


def mostrarCadena(cadena):
    for i in lista:
        print(i)
        cadena+=str(i)+coma
    return cadena

#Punto c
def listaInversa(lista):
    lista.sort(reverse=True)
    lista2=lista
    return lista2

#Punto d
def menu(lista):
    menu = int(input("seleccione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu> 2:
        print('Digite el numero 1 o 2')
        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu == 1:
        letra = input("Introduzca la palabra que desea buscar en la lista: ")
        for i in lista:
            if i == letra:
                print('es igual ')
            else:
                print('no es igual')
        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    if menu == 2:
        print('Vuelva pronto')

#Punto e
def contar(lista):
    letra = input("Introduzca la palabra que este dentro de la lista para contar sus silabas: ")
    for i in lista:
        if i == letra:
            verdad=len(i)
            print(f'{verdad}')
        else:
            print(f"NULL")

#base
lista=['Gabriel','Steven','Cristian','Andrea','Yessica','Rayo','Efrolin','Almeja','Petro','Petrosky']
cadena=""
coma=","

print("\n El programa mostrara en una variable la lista \n")

cadena =mostrarCadena(cadena)
print(f"{cadena}")

print("\n Se imprimira la lista en de manera desendente alfabeticamente \n")

lista2 =listaInversa(lista)
print(f"{lista2}")
# OJO al buscar en la lista queda ordenada de mayor a menor Z a A
print("\n El programa dira si ese nombre esta dentro de la lista \n")

menu(lista)

print("\n El programa contara las silabas \n")

contar(lista)

print("finalizo el programa")


 

