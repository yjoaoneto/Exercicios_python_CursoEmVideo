a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificar o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O\033[1;33m menor\033[m valor é {}!'.format(menor))
print('O\033[1;34m maior\033[m valor é {}!'.format(maior))
