import re

userString = input("Introduzca una cadena de texto: ")
if re.search("[@$?¡\-_\.,]", userString):
    print("Se han encontrado caracteres no alfabéticos")
else:
    print("✔")