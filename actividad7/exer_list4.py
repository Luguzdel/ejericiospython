from re import X
list=[]
value=int(input("Digita la lista: "))
while value in range(5):
    list.append(value)
    if list < 0:
        b=int(input("Digita un número positivo: "))
        print(b)
    

