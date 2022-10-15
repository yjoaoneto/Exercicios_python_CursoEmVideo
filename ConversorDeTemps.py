c =float(input('Informe a temperatura em C°: '))
f = (9 * c) / 5 + 32
print('A\033[31m temperatura\033[m de\033[32m {}C°\033[m corresponde a\033[34m {}F°\033[m.'.format(c,f))
