# considere a empresa de telefonia tchau.
# abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto. entre 200 e 400
# minutos,o preço é R$ 0,18. Acima de 400 minutos o preço por minuto é de
# R$ 0,15. Calcule sua conta de telefone.

valor = float(input('Preço da conta: '))

if (valor < 200):
    cobra = (valor * 0.20)
    print('Valor gasto: R$ %6.2f' %cobra)

if (valor > 200 and valor < 400):
    cobra = (valor * 0.18)
    print('Valor gasto: R$ %6.2f' %cobra)

if (valor > 400):
    cobra = (valor * 0.15)
    print('Valor gasto: R$ %6.2f' %cobra)

# o programa poderia ser feito da seguinte forma:
# minutos = int(input("minutos utilizados: "))
# if minutos < 200:
#      preco = 0.20
# else:
#      if minutos <=400:
#          preco = 0.18
#      else:
#          preco = 0.15
# print("conta telefonica: R$%6.2f" % (minutos * preco))

            



            




            
