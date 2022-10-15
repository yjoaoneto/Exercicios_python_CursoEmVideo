from random import choice
n1 =str(input('Primeiro aluno: '))
n2 =str(input('Segundo aluno: '))
n3 =str(input('Terceiro aluno: '))
n4 =str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno\033[33m escolhido\033[m foi\033[36m {}\033[m'.format(escolhido))

