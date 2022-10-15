n = str(input('Digite seu nome: ')).strip()
print('Seu nome tem\033[36m silva\033[m?: {}'.format('SILVA' in n.upper()))

