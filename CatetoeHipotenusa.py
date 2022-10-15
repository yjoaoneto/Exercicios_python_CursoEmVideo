from math import hypot
co =float(input('Cateto oposto: '))
ca =float(input('Cateto adjacente: '))
hi = math.hypot(ca,co)
print('A\033[33m hipotenusa\033[m vai medir\033[35m {:.2f}\033[m'.format(hi))
