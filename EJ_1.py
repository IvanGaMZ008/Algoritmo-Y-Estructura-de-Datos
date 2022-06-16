# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:01:08 2022

@author: CrIva
"""
"""
1.Lea los nombres y las edades de diez alumnos, y que los datos se almacenen en dos vectores, y 
con base en esto se determine el nombre del alumno con la edad mayor del arreglo.
"""

c=1
Alumnos=[]
Edad=[]
n=int(input("Ingrese el numero de alumnos:"))
        
for i in range(0,n,1):
  print("Alumno No.",c,end=" ")
  alumno=str(input("Ingrese el nombre del alumno:"))
  print("Alumno No.",c,end=" ")
  edad=float(input("Ingrese la edad del alumno:"))
  Alumnos.append(alumno)
  Edad.append(edad)
  c=c+1
 
# La función  zip(Elemento Vector Alumno,Elemento Vector Cal) toma como argumento dos o más 
# objetos iterables (idealmente cada uno de ellos con la misma cantidad de elementos) y 
# retorna un nuevo iterable cuyos elementos son tuplas que contienen un elemento de cada 
# uno de los iteradores originales.
Union=list(zip(Alumnos, Edad))
#Python tiene una función predefinida llamada max() que devuelve el valor máximo de una lista.
#El argumento key acepta una función lambda y permitirá a la función max() devolver un par 
#clave-valor(Nombre-Edad), en este caso se busca el alumno con mayor edad 
#por eso el item[1] que corresponde a las edades dentro de los elementos del vector Union
Vmax=max(Union, key=lambda item: item[1])
print("El alumno con mayor edad es",Vmax[0], "con una edad de",Vmax[1],"años") 