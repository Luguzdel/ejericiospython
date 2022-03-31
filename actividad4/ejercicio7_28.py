valor_compra= int(input("Ingrese el valor total de su compra: "))
cliente= input("Ingrese el color de su balota: ")
roja= ("100% de descuento")
verde= valor_compra-(valor_compra*0.5)
blanco= valor_compra-(valor_compra*0.3)
negra= valor_compra-(valor_compra*0.2)
amarilla= valor_compra-(valor_compra*0.1)

if valor_compra > 50000:
    if cliente == ("roja"):
        print("Su balota es roja, tiene 100% de descuento y el valor a pagar es 0")
    elif  cliente== ("verde"):
        print(f'Su balota es verde, tiene 50% de descuento y el valor a pagar es: {verde}')  
    elif  cliente== ("blanco"):
            print(f'Su balota es blanco, tiene 30% de descuento y el valor a pagar es: {blanco}')     
    elif  cliente== ("negra"):
        print(f'Su balota es negra, tiene 20% de descuento y el valor a pagar es: {negra}')    
    elif  cliente== ("amarilla"):
        print(f'Su balota es amarilla, tiene 10% de descuento y el valor a pagar es: {amarilla}')
else:
    print(f'No aplica descuento, el valor a pagar es: {valor_compra}')        