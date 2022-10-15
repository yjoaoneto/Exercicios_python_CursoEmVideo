km =float(input('Qual a distância da sua viagem ?'))

print('Você está prestes a iniciar uma viagem de\033[1;34m {:.2f}km\033[m'.format(km))
if km <= 200:
    preço = km * 0.50

else:
    preço = km * 0.45
print('O preço da sua passagem de ônibus será de\033[1;34m R${:.2f}\033[m'.format(preço))