n =int(input('Digite um valor: ' ))
r = n ** (1/2)
print('O dobro de\033[33m {}\033[m vale\033[m {}\033[m. \n O triplo vale \033[32m{}\033[m. \n E a raiz quadrada  é\033[32m {:.2f}\033[m.'.format(n,(n*2),(n*3),(r)))

