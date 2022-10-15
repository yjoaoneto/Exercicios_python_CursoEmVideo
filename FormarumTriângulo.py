#Condição da existência de um triângulo
#Se a soma de duas retas é maior que o valor da terceira, o triângulo pode existir
print('-=-' * 20)
print('Para saber se é possível construir um triâmgulo, digite os valores das retas abaixo: ')
print('-=-' * 20)
r1 =float(input('Primeira reta: '))
r2 =float(input('Segunda reta: '))
r3 =float(input('Terceira reta: '))
if r1 + r2 >= r3 and r1 + r3 >= r2 and r2 + r3 >= r1:
    print('\033[1;32mÉ POSSÍVEL\033[m construir um \033[34mtriângulo\033[m!')
else:
    print('\033[1;31mNÃO é POSSÍVEL\033[m construir um \033[34mtriângulo\033[m!')

