from random import shuffle
n1 =str(input('Primeiro aluno: '))
n2 =str(input('Segundo aluno: '))
n3 =str(input('Terceiro aluno: '))
n4 =str(input('Quarto aluno: '))
lista =[n1,n2,n3,n4]
ordem = shuffle(lista)
print('A\033[33m ordem\033[m de apresentação do trabalho será\033[34m {}\033[m'.format(lista))
