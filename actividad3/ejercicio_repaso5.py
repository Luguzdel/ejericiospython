palabra= input('introduzca una palabra: ')
long_pala= len(palabra)
vocal_a= palabra.count('a')
vocal_e= palabra.count('a')
vocal_i= palabra.count('a')
vocal_o= palabra.count('a')
vocal_u= palabra.count('a')

metrica= long_pala * (vocal_a + vocal_e + vocal_i + vocal_o + vocal_u)
print (metrica)