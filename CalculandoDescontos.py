p =float(input('Qual o preço do produto? '))
vl = p - (p * 5 / 100)
print('O\033[32m valor\033[m final do produto com o desconto de\033[34m {}%\033[m é de {:.2f}.'.format(5,vl))