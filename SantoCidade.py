n =str(input('Digite o nome da sua cidade: ')).strip()
print('Sua cidade começa ou não com\033[34m ''SANTO''\033[m?')
print(n[:5].upper() == 'SANTO')



