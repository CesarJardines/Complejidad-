import os
import itertools
import random
import src.utils as foo

from src.graph import Graph
from random import randrange

#lista de entradas en formato .txt para evaluar (se puede ver en la carpeta input)
lista = ["input_1.txt","input_2.txt","input_3.txt","input_4.txt","input_5.txt"]
#variable aleatorea para agarrar una entrada de manera random 
ran = randrange(4)

def main():
	#Buscamos la grafica a evaluar en nuestra carpeta input
	txt_file = r"input/" + lista[ran]
	#Punto de la grafica por el que empezaremos
	Npadre = "1"
	aux = False

	#Creamos la grafica con nuestra entrada seleccionada
	initial_g = foo.creaGrafica(txt_file)

	#Creamos el MST T de G
	mst = foo.get_mst(initial_g)
	#Conseguimos los grados de los nodods de nuestra graficaM MST T de G
	mst_grado = foo.get_grados(mst)
	#Conseguimos los nodos impares
	grado_odd = foo.get_n_odd(mst_grado)
	#Generamos la subgrafica
	subgrafica = foo.crearSubgrafica(initial_g, grado_odd)
	#Adquirimos el peso minimo de nuestra convinacion de la subgrafica ya antes adquirida
	pesoMinNodos = foo.combinacionPesosMin(subgrafica)
	#Unimos los caminos de la G
	union_graph = foo.union(mst, pesoMinNodos)
	#Consefuimos el camino euleriano
	caminoEuleriano = union_graph.get_euler_tour(Npadre)
	camino = []
	for i in caminoEuleriano:
		camino.append(i)

	if aux:
		gEuleriana = Graph()
		for i in camino:
			gEuleriana.add_edge(i[0], i[1], initial_g.get_edge_weight(i[0], i[1]))
			

	camino = list(itertools.chain.from_iterable(list(camino)))
	camino = list(dict.fromkeys(camino).keys())
	camino.append(Npadre)
	#Imprimimos por consola
	print("**********************************************************************************")
	print(f"\nLa grafica de entrada esta dada por el archivo {lista[ran]} de la carpeta input")
	print("**********************************************************************************")
	print(f"\nLa salida de nuestra grafica {lista[ran]} es:")
	print(f"\n π': {camino}\n")
 
  

main()
