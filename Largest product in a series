totales = []
resultados = []
iteraciones = int(input())
for x in range(0,iteraciones):
	aux=0
	var = list(map(int,raw_input("\n").split(" ")))
	numero = list(map(long,raw_input("\n")))
	for y in range(0,var[0]-(var[1]-1)):
		aux=numero[y]
		for z in range(y+1,y+var[1]):
			aux=long(aux*numero[z])
			if (z==((y+var[1])-1)):
				totales.append(aux)
	resultados.append(max(totales))
	del totales[:]
for h in resultados:
	print "\n",h
