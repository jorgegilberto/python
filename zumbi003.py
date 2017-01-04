#programa: pergunte a velocidade de um carro, supondo um valor inteiro.
# Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Neste caso, exiba o valor da multa, cobrando R$ 5,00 por
# km acima de 110.

a = int(input('Velocidade: '))

if a < 110:
    print('Voce esta abaixo do limite de velocidade')
if a >= 110:
    print('Seu carro será multado.')
    multa = (a - 110) * 5
    print('E sua multa foi de R$ %5.2f ' %multa)
