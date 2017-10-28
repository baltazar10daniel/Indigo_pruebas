historico = []
resultado = []
casos = int(input())
for x in range(0,casos):
	j=0
	numero = long(input("\n"))
	for y in xrange(100,1000):
		for z in xrange(y+1,1000):
			mult=y*z
			if mult>(numero-10000) and mult<numero:
				posibles=list(map(long,str(mult)))
				if posibles==posibles[::-1]:
					historico.append(long(mult))
					del posibles[:]
	resultado.append(max(historico))
	del historico[:]
for i in resultado:
	print "\n",i
