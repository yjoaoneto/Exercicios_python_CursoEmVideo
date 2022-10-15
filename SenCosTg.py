from math import cos, sin, tan, radians
ang =float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('O\033[33m ângulo\033[m de\033[31m {}\033[m tem o\033[36m seno\033[m de\033[31m {:.2f}\033[m, o\033[34m cosseno\033[m de\033[32m {:.2f}\033[m e a\033[33m tangente\033[m de\033[32m {:.2f}\033[m.'.format(ang, seno,cos,tg))
