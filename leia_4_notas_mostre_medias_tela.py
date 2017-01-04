# fazer um programa que leia 4 notas, mostre as notas e a média na tela.
'''
x = 0
vetor = []
media = 0
total=1
while x < 4:
    nota=float(input("Nota: "))
    vetor.append(nota)
    media = media + vetor[x]
    x+=1
total=media/4
print("A media foi: ", total)
print("As notas: ", vetor)
''' 
# outra forma de se resolver este problema, de acordo com o instrutor

notas = []
i = 1
while i < 4:
    n =float(input("Nota: "))
    notas.append(n)
    i+=1
soma = 0
i = 0

while i <= 3:
    soma += notas[i]  # o programa esta com erro aqui, nao detectado por mim
    i+=1
print("Notas: ", notas)
print("Média: %4.2f " %(soma/4))












