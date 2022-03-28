dni= input("introduzca su identificacion: ")
nif= "TRWAGMYFPDXBNJZSQVHLCKE"
digitos= nif [int(dni) % 23]
completo=dni + digitos

print(f'{completo}')