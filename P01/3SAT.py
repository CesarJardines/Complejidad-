from random import randrange

print("**********************************************************************************")
print("*         Hola, he creado 10 variables y les he asigando valores booleanos       *")
print("*                    estas son sus respectivas asignaciones                      *")
print("**********************************************************************************")
#Le damos aleatoreamente valores a las variables, estos valores solo pueden tener 1 y 0. Haciendo referencia
#a el estado True y False
a = randrange(2)
b = randrange(2)
c = randrange(2)
d = randrange(2)
e = randrange(2)
f = randrange(2)
g = randrange(2)
h = randrange(2)
i = randrange(2)
j = randrange(2)

#Fase adivinadora del algortimo // Mostramos en terminal caules son las respectivas asignaciones que nuestro codigo escogió
print("A= " + str(a) + " B= " + str(b)+ " C= " + str(c) + " D= "+ str(d) + " E= " +str(e)+" F= "+str(f)+" G= "+str(g)+" H= "+str(h)+" I= "+str(i)+" J= "+str(j))

#Generamos valores del 0 al 10 para poder usar listas paralelas y poder imprimir las asiganciones de las clausulas que generó el programa
a1 = randrange(9) #variables primas
b1 = randrange(9)
c1 = randrange(9)
d1 = randrange(9)
e1 = randrange(9)
f1 = randrange(9)
g1 = randrange(9)
h1 = randrange(9)
i1 = randrange(9)
j1 = randrange(9)

#listas paralelas el cual la posición de la ListaA[x] está ligado a la posición de listaB[x] donde x es el numero generado en las variables primas 
listaA=[a,b,c,d,e,f,g,h,i,j]
listaB=["a","b","c","d","e","f","g","h","i","j"]
#el programa genera 5 clausulas, cada que se ejecute el programa dará clausulas distintas
print("He generado 5 clausulas con las siguentes variables")

#Muestra las clausulas con las variables generadas
print("("+ listaB[a1] + listaB[b1] + listaB[c1]+")"+ "," + "(" + listaB[d1]+ listaB[e1] + listaB[f1]+ ")"+ ","+ "(" +listaB[g1]+ listaB[h1]+ listaB[i1]+")"+ ","+ "(" +listaB[a1]+ listaB[d1]+ listaB[g1]+")"+ ","+ "(" +listaB[h1]+ listaB[h1]+ listaB[i1]+")")

#Fase verificadora del algortimo
if (listaA[a1] or listaA[b1] or listaA[c1]) and (listaA[d1] or listaA[e1] or listaA[f1]) and (listaA[g1] or listaA[h1] or listaA[i1]) and (listaA[a1] or listaA[d1] or [g1]) and (listaA[h1] or listaA[h1] or listaA[i1]):
	print("La clausula generada ES satisfacible! \n los valores de las variables son: ")
	print( listaB[a1] + "="+ str(listaA[a1]) +  listaB[b1] + "="+ str(listaA[b1])  + listaB[c1]+ "=" + str(listaA[c1])  + listaB[d1]+ "="+   str(listaA[d1])  + listaB[e1]+ "="+ str(listaA[e1])  + listaB[f1]+ "=" + str(listaA[f1]) + listaB[g1]+ "=" + str(listaA[g1]) + listaB[h1]+ "=" +  str(listaA[h1]) + listaB[i1]+ "="+ str(listaA[i1]) + listaB[j1]+ "=" +  str(listaA[j1]))
else:
	print("La solución NO ES satisfacible \n los valores de las variables son: ")
	print( listaB[a1] + "="+ str(listaA[a1]) +  listaB[b1] + "="+ str(listaA[b1])  + listaB[c1]+ "=" + str(listaA[c1])  + listaB[d1]+ "="+   str(listaA[d1])  + listaB[e1]+ "="+ str(listaA[e1])  + listaB[f1]+ "=" + str(listaA[f1]) + listaB[g1]+ "=" + str(listaA[g1]) + listaB[h1]+ "=" +  str(listaA[h1]) + listaB[i1]+ "="+ str(listaA[i1]) + listaB[j1]+ "=" +  str(listaA[j1]))


