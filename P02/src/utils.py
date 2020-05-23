import copy
import networkx as nx
from src.graph import Graph

#Funcion que nos ayuda a construir una grafica segun un .txt
def creaGrafica(txt_file: str):
    nodos = []
    with open(txt_file) as file:
        lineaParse = file.readline()
        while lineaParse:
            #Dejamos de parsear el .txt hasta que se encientre #
            if "#" not in lineaParse:
                n_info = lineaParse.replace("\n", "").split(",")
                nodos.append((n_info[0], n_info[1], n_info[2]))
            lineaParse = file.readline()
    #Generamos los nodos y anadimos para crear a G
    if len(nodos) > 0:
        g = Graph()
        g.add_node_list(nodos)
        return g

#Funcion que obtiene el MST T de nuestra grafica G
def get_mst(graph: Graph):
    #implementacion Kruskal
    aristas = graph.get_edges()
    weighted_aristas = {}
    for (u, v) in aristas:
        weighted_aristas[(u, v)] = int(graph.get_edge_weight(u, v))

    #Ordenamos nuestros nodos por peso
    weighted_aristas = sorted(weighted_aristas.items(), key=lambda x: x[1])

    mst = Graph()
    nodes = []
    for i in weighted_aristas:
        u, v = i[0]
        mst.add_edge(u, v, graph.get_edge_weight(u, v))
        try:
             nx.algorithms.find_cycle(mst.get_graph())
             mst.get_graph().remove_edge(u, v)
        except nx.NetworkXNoCycle:
            nodes.append(u)
            nodes.append(v)

    return mst

#Getter grados de nuestra G
def get_grados(graph: Graph):
    grad = {}
    for i in graph.get_degree():
        grad[i[0]] = i[1]

    return grad

#Getter de nodos impares
def get_n_odd(degrees: dict):
    impares = {}

    for i in degrees.keys():
        if (degrees[i]%2) !=0:
            impares[i] = degrees[i]

    return impares

#Añadimos nuestras tuplas de aristas a un diccionario para una mejor representación
def convert_edges_tuples_to_dict(nodes, edges_tuples):
    aristas = {}
    #Añadimos los nodos como llaves del dicc
    for i in nodes:
        aristas[i] = []

    for e in aristas_tuplas:
        aristas[e[0]].append((e[1]))
        aristas[e[1]].append((e[0]))

    return aristas

#Funcion para generar subgrafica de G como parametro
def crearSubgrafica(graph: Graph, nodosRestantes):
    subgra = nx.Graph(graph.get_graph().subgraph(nodosRestantes))
    return Graph(subgra)

#Funcion para extraer aquellos nodos adyacentes que tengan peso minimo de entre sus vecinos
def combinacionPesosMin(graph: Graph):
    #Creamos una nueva grafica con pesos negativos
    nuevaG = Graph()
    for i in graph.get_edges():
        nuevaG.add_edge(i[0], i[1], -int((graph.get_edge_weight(i[0], i[1]))))
    vecino = nx.max_weight_matching(nuevaG.get_graph(), maxcardinality=True)
    nodoVecino = Graph()
    for j in vecino:
        nodoVecino.add_edge(j[0], j[1], graph.get_edge_weight(j[0], j[1]))

    return nodoVecino

#Funcion para unir G y crear un camino 
def union(graph1: Graph, graph2: Graph):
    caminoUnionG1G2 = Graph(multi_graph=True)
    for i in graph1.get_edges():
        caminoUnionG1G2.add_edge(i[0], i[1])

    for e in graph2.get_edges():
        caminoUnionG1G2.add_edge(e[0], e[1])

    return caminoUnionG1G2

#Funcion para obtener el costo total 
def getCosto(graph, path):
    peso = 0
    for i in range(1, len(path)):
        peso += int(graph.get_edge_weight(path[i-1], path[i]))
    return peso
