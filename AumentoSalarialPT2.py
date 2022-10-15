salario =float(input('Qual o seu salário? '))
if salario >= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario +(salario * 10 /100)
print('Quem recebia\033[1;31m R${:.2f}\033[m agora recebe\033[1;32m R${:.2f}'.format(salario,novo))
