d =float(input('Uma distância em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A medida de\033[32m {}m\033[31m corresponde a\033[36m \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm.'.format(d,km,hm,dam,dm,cm,mm))
