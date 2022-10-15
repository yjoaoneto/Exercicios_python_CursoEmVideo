from time import sleep
from random import randint
computador = randint(0, 5) #Faz o computador 'pensar'
print( '-=-' * 20 )
print('Vou pensar em um número entre 0 e 5, consegue adivinhar?' )
print( '-=-' * 20 )
jogador = int(input('Em qual número estou pensei? ')) #Jogador tenta adivinhar
print('\033[35mPROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[32mBOAAAA\033[m,você conseguiu adivinhar!')
else:
    print('\033[31mERROUUUU\033[m!Eu estava pensando no número \033[32m{}\033[m e não no \033[31m{}\033[m!'.format(computador,jogador))

