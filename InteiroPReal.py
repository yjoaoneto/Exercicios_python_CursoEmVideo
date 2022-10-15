from math import trunc
nr =float(input('Digite um número real: '))

print('O valor\033[32m inteiro\033[m de\033[31m {}\033[m é:\033[33m {:.2f}\033[m. '.format(nr,trunc(nr)))
