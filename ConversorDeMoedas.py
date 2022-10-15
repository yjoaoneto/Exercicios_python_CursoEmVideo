r =float(input('Quanto dinheiro você tem? R$ '))
d = r / 5.08
e = r / 6
print('Com\033[33m R${:.2f}\033[m,você consegue comprar \033[34mUS${:.2f}\033[m e\033[m £{:.2f}\033[35m.'.format(r,d,e))
