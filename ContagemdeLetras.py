n =str(input('Digite uma frase qualquer: '))
print('Na sua\033[1;36;30m frase\033[m a letra ''a''aparece \033[33m{}\033[m vezes'.format(n.count('a')))
print('A letra ''a'' aparece pela primeira vez na posição \033[35m{}\033[m'.format(n.find('a')))
print('A letra ''a'' aparece pela última vez na posição \033[32m{}'.format(n.rfind('a')))
