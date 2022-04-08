MAX=9;
CARACTER="1"

for i in range(MAX):
    buffer = CARACTER * (i+1)
    blank = " " * (MAX - (i+1))
    print(blank + buffer + "." + buffer)