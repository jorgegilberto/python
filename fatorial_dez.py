#calcular o fatorial de dez

n = 1
fat = 10
res = 10
while  n != 10:
    res = res * (fat - n)
    n = n + 1
    
print("Fatorial de 10 é: %d" %res)
