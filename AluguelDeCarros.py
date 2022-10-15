d = float(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos quilômetros você andou? '))
p = (60 * d) + ( 0.15 * k )
print('O\033[1;34m valor\033[m total a pagar pelo carro é de\033[32m R${}\033[m.'.format(p))
