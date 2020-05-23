import random

def aproxSubsetSum(S,t,epsilon):
	n = len(S)
	#listas ordenadas que se iran creando.
	listas = [[0]]

	for i in range(1, n + 1):
		#Necesitamos hacer una copia del arreglo
		#para poder usarlo en mergelist.
		lprima = listas[i - 1].copy()

		#Hacemos la suma de valores en la copia
		sumaValor(lprima, S[i - 1])

		#Juntamos y ordenamos las listas.
		mergedList = mergeLists(listas[i - 1], lprima)

		#Calculamos el factor y hacemos trim de la lista
		#ordenada.
		factor = epsilon / (2 * n)
		trimedList = trim(mergedList, factor)

		#Quitamos los valores mayores a t.
		trimedList = quitaValoresMayores(trimedList, t)

		#Insertamos la lista en la lista de ordenadas.
		listas.insert(i,trimedList)

	#Regresamos la lista con la respuesta.
	return listas[n].pop()


#Funcion auxiliar que suma un valor a todas las entradas de un arreglo.
def sumaValor(lista, valor):
	for i in range (len(lista)):
		lista[i] += valor



#Funcion auxiliar para quitar valores mayores en una lista de números mayores que t.
def quitaValoresMayores(lista, t):
	listaNueva = [i for i in lista if i < t]
	return listaNueva


#Funcion auxiliar mergeLists que recibe dos listas,las une y después las ordena en órden creciente.
def mergeLists(lista1, lista2):
	merged = list(set(lista1 + lista2))
	merged.sort()
	return merged


#Funcion auxiliar trim, que "recorta" una lista conforme al factor recibimos.
def trim(lista, factor):
	m = len(lista)

	listaNueva = [lista[0]]
	last = lista[0]

	for i in range(1, m):
		#lista[i] >= last ya que lista está ordenada
		if (lista[i] > last * (1 + factor)):
			listaNueva.append(lista[i])
			last = lista[i]
	return listaNueva

def main():
	numeros = []
	print("Se mostrara la ejecución para el conjunto de números:")

	#Conjunto aleatorio.
	for i in range(0,15):
		numeros.append(random.randint(1, 200))

	print(numeros)
	print("\n")
	print("*************************************************************")
	print("Se ejecutará el algortimo con 3 valores distintos de epsilon:")
	print(".25, .50 y .75 \n")
	print("*************************************************************")

	print("El valor de t será: 500")

	print("Con epsilon = .25 y t = 500 la aproximación es:")
	aprox1 = aproxSubsetSum(numeros, 500, .25)
	print(aprox1)
	print("\n")

	print("Con epsilon = .50 y t = 500 la aproximación es:")
	aprox1 = aproxSubsetSum(numeros, 500, .50)
	print(aprox1)
	print("\n")

	print("Con epsilon = .75 y t = 500 la aproximación es:")
	aprox1 = aproxSubsetSum(numeros, 500, .75)
	print(aprox1)
	print("\n")

main()
