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


# modifique o programa da empresa tchau para
# uma promoção onde a tarifa é de R$ 0,08
# quando você utiliza mais que 800 minutos


minutos = int(input("minutos utilizados: "))

if   minutos < 200:
    preco = 0.20
elif minutos <=400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08

print ("conta telefonica: R$%6.2f" % (minutos * preco))
