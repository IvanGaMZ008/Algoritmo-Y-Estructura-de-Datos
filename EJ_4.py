# -*- coding: utf-8 -*-
"""
Created on Sun May  8 22:39:42 2022

@author: CrIva
"""
"""
Se tiene un arreglo de 15 filas y 12 columnas. Realice un algoritmo que permita leer el arreglo y que 
calcule y presente los resultados siguientes: 
(a)El menor elemento del arreglo;(b)la suma de los elementos de las cinco primeras filas del arreglo; 
"""

#y (c)el total de elementos negativos en las columnas de la quinta a la nueve. 
import numpy as np 
sumaFilas=[]
Count=0

Matriz = np.random.randint(-100,100, size=(15, 12)) 
#Lafuncion np.random.randint(Numero_inicial,numero_final,tamaño=(fila,columna,) se utilizo para crear
#una matriz especifica rellenada con numeros dentro de un rango 
print(Matriz)
#(a)El menor elemento del arreglo
min_valor=np.amin(Matriz)#La funcion np.amin() se utiliza para obtener el el elemnto menor de la matriz
print("El menor elemento del arreglo:",min_valor,), print(sep="\n") 
#b)la suma de los elementos de las cinco primeras filas del arreglo; 
for i in range(0,5,1):
 Fila=sum(Matriz[i])
 sumaFilas.append(Fila)
 
print("El siguiente vector muestra la suma de cada fila: ",sumaFilas)
print("la suma de la primera fila es:",sumaFilas[0])
print("la suma de la segunda fila es:",sumaFilas[1])
print("la suma de la tercera fila es:",sumaFilas[2])
print("la suma de la cuarta fila es:",sumaFilas[3])
print("la suma de la quinta fila es:",sumaFilas[4])
print("La suma total de los elementos de las 5 primeras filas es:",sum(sumaFilas)), print(sep="\n")
#(c)el total de elementos negativos en las columnas de la quinta a la nueve. 

for i in range (4,9,1):
  Columnas=Matriz[:, i]
  for j in range(0,15,1):
      if Columnas[j]< 0:
       Count=Count+1 

print("El total de elementos negativos en las columnas 5 a 9 es: ", Count) 