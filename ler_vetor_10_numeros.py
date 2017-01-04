# programa que leia um vetor de 10 numeros reais e mostre-so na ordem inversa

vetor = []
x = 1

while x <= 10:
    n = float(input("Digite um número: "))
    vetor.append(n)
    x+=1
i = 9
while i >= 0:
    print("Vetor Lido: ", vetor[i])
    i-=1
    
