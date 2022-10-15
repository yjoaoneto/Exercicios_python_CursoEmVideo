nmr =int(input('Digite um número e eu direi se ele é par ou ímpar: '))
resultado = nmr % 2
if resultado == 0:
    print('O número digitado é\033[35m par\033[m')
else:
    print('O número digitado é\033[33m ímpar\033[m')
