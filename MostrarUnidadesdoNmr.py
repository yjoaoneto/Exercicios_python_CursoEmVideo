num =int (input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('\033[32m Unidade\033[m: {}'.format(u))
print('\033[33m Dezena\033[m: {}'.format(d))
print('\033[34m Centena\033[m: {}'.format(c))
print('\033[35m Milhar\033[m: {}'.format(m))


