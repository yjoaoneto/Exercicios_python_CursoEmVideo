s =float(input('Qual o seu salário antes do aumento? '))
a = s + (s * 15 / 100)
print('Seu\033[33m salário\033[m com um\033[32m aumento\033[m de 15% é de\033[35m {:.2f}\033[m'.format(a))

