km =int(input('Qual a velocidade em Km/h seu carro ultrapassou na BR-230? '))
multa = 7 * (km - 80)
if km <= 80:
    print('Você estava no limite de velocidade! Tenha um\033[4;35m bom dia\033[m!')
else:
    print('Você terá que pagar uma\033[31m multa\033[m de R${:.2f}. Seja mais\033[4;33m reponsável no trânsito\033[m!'.format(multa))

