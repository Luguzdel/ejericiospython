numero1=int(input("Introduzca el primer número: "))
numero2=int(input("Introduzca el segundo número: "))
numero3=int(input("Introduzca el tercer número: "))

if numero1 < numero2 and numero3:
    print(f'numero menor es: {numero1}')
elif numero2 < numero1 and numero3:
     print(f'numero menor es: {numero2}')   
elif numero3 < numero1 and numero2:
     print(f'numero menor es: {numero3}')    

