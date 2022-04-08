n = int(input("introduzca un número: "))
producto = 1

for x in range(n):
    producto *= ((x+1)**2)

print(producto)    