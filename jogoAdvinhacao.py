import random
print('Tente advinhar o numero no qual eu estou pensando...')
print('Pense em um numero de 0 a 5')
sorteio = random.randint(1,5)
pessoa = int(input('Digite um numero: '))

while pessoa != sorteio:
    pessoa = int(input('Voce errou, tente novamente: '))
print('Voce acertou!!!, o numero que eu pensei e que voce digitou foi {}'.format(sorteio))


