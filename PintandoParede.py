l =float(input('Largura da parede: '))
a =float(input('Altura da parede: '))
ap = a * l
tn = (a * l) / 2
print('A sua parede tem a dimensão de\033[32m {:.2f}x{:.2f}\033[m e sua área é\033[33m {:.2f}m\033[m. \n Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(l,a,ap,tn))
