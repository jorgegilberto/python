# calcula a media de 5 notas

''' UMA FORMA DE ESCREVER O PROGRAMA, ABAIXO:
total = 1
resul=1
media = (10, 10, 10, 5, 5)
total = media[0] + media[1] + media[2] + media[3] + media[4]
resul=total/5

print(resul)
'''
# outra forma de escrever o programa

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print("Média: %5.2f" %(soma/x))
