#Programa para ler um vetor de 5 números e mostre o vetor.

vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um número: "))
    vetor.append(n)
    i+=1
print("Vetor lido: ", vetor)
