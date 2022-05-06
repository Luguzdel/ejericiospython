l=[]
limit=int(input("Por favor digita el número límite de tu lista: "))
for i in range (limit):
    value=int(input("Digita los valores: "))
    l.append(value**2)
print(l)