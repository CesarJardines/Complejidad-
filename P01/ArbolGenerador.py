from random import choice
import random

print("**********************************************************************************")
print("*     Hola, he creado 5 vertices con aristas conectadas con los vertices sig     *")
print("*                    estas son sus respectivas asignaciones                      *")
print("*                           {Vi tiene arista con Vj}                             *")
print("**********************************************************************************")

#Al vertice Vn le asigna una arista a otro vertice n de manera aleatorea
v1 = choice([i for i in range(1,7) if i not in [1]])
v2 = choice([i for i in range(1,7) if i not in [2]])
v3 = choice([i for i in range(1,7) if i not in [3]])
v4 = choice([i for i in range(1,7) if i not in [4]])
v5 = choice([i for i in range(1,7) if i not in [5]])
v6 = choice([i for i in range(1,7) if i not in [6]])
#Generamos mas aristas y que no se repitan con Vn
v1p = choice([i for i in range(1,7) if i not in [1,v1]])
v2p = choice([i for i in range(1,7) if i not in [2,v2]])
v3p = choice([i for i in range(1,7) if i not in [3,v3]])
v4p = choice([i for i in range(1,7) if i not in [4,v4]])
v5p = choice([i for i in range(1,7) if i not in [5,v5]])
v6p = choice([i for i in range(1,7) if i not in [6,v6]])
#Generamos mas aristas y que no se repitan con las Vnp
v1p1 = choice([i for i in range(1,7) if i not in [1,v1p]])
v2p2 = choice([i for i in range(1,7) if i not in [2,v2p]])
v3p3 = choice([i for i in range(1,7) if i not in [3,v3p]])
v4p4 = choice([i for i in range(1,7) if i not in [4,v4p]])
v5p5 = choice([i for i in range(1,7) if i not in [5,v5p]])
v6p6 = choice([i for i in range(1,7) if i not in [6,v6p]])

print("Hemos generado una grafica aleatoreamente con los vertices")
print("V1 CON ARISTAS A V" + str(v1p1)+ " V"+ str(v1)+ " V" + str(v1p) + "\n V2 CON ARISTAS A  V" + str(v2p2)+ " V" + str(v2)+ " V"  + str(v2p) + "\n V3 CON ARISTAS A  V"+ str(v3p3)+ " V"+ str(v3)+ " V"  + str(v3p) + "\n V4 CON ARISTAS A  V"+ str(v4p4)+ " V"+ str(v4)+ " V"  + str(v4p) + "\n V5 CON ARISTAS A  V"+ str(v5p5)+ " V"+ str(v5)+ " V"  + str(v5p)+ "\n V6 CON ARISTAS A  V" + str(v6p6) + " V" + str(v6) + " V" + str(v6p))


lista = [1,2,3,4,5,6]
listav1p1=[v1p1,v2p2,v3p3,v4p4,v5p5,v6p6]
listav1 = [v1,v2,v3,v4,v5,v6]
listav1p = [v1p,v2p,v3p,v4p,v5p,v6p]

salida=[]

#creamos un subarbol de manera aleatorea(Fase adivinadora)
for i in range(6):
	if(listav1p1[i] <= listav1[i] and listav1p1[i] <= listav1p[i]): 
		salida.append(listav1p1[i])
	else:
		if(listav1[i] <= listav1p1[i] and listav1[i] <= listav1p[i]):
			salida.append(listav1[i])
		else:
			if(listav1p[i] <= listav1[i] and listav1p[i] <= listav1p1[i]):
				salida.append(listav1p[i])

salida.sort()
n = 1
for i in range(6):
	if salida[i] != n:
		salida[i] = i+1%6

#Verificamos si el ejemplar es satisfacible y dira si lo es o no (Fase Verificadora)
if(salida[0]==1 and salida[1]==2 and salida[2]==3 and salida[3]==4 and salida[4]==5 and salida[5]==6):
	print(" ")
	print("Hemos generado una subgrafica")
	print("*********************************************")
	print("****El ejemplar Si es satisfacible        ***")
	print("*********************************************")
	print(" ")
else:
	print("Hemos generado una subgrafica")
	print("**No es un ejemplar satisfacible**")
random.shuffle(salida)

print("subarbol generado con vértices pasa por: " + str(salida))



