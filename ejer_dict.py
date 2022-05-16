month= dict(
    enuary=150,
    february=234,
    march=350,
    april=100,
    may=420,
    june=634,
    july=705,
    august=878,
    september=923,
    october=3056,
    november=1114,
    dicember=1200,
)
total=0
max_value=max(month.keys(), key=lambda k:month[k])
print(f'El mes con mayor producción es:',max_value, month[max_value])

min_value=min(month.keys(), key=lambda k:month[k])
print(f'El mes con mayor producción es:',min_value, month[min_value])

for i in month.values():
    total += i
average= total/12
print('El promedio es: ', average)


for i in month.keys():
    if month[i]>=average:
        print('Los meses que están por encima del promedio son: ',i)

    
for i in month.keys():
    if month[i]<=average:
        print('Los meses que están por debajo del promedio son: ',i)
    

