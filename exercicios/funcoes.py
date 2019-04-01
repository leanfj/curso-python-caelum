def divisao(x, y):
    resultado = x // y
    return resultado


def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    # print(velocidade)
    return velocidade


print('Velocidade média: {}\n'.format(velocidade_media(100, tempo=20)))
print('Velocidade média: {}\n'.format(velocidade_media(200, tempo=5)))


def soma(x, y):
    resultado = x + y
    return resultado


def subtracao(x, y):
    resultado = x - y
    return resultado


def calculadora(x, y):
    print('Soma: {}\n'.format(soma(x, y)))
    print('Substração: {}\n'.format(subtracao(x, y)))


calculadora(2, 4)
