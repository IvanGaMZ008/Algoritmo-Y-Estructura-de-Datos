# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:50:03 2022

@author: CrIva
"""
"""
2.Modifique el problema anterior, considerando que el vector tiene N elementos 
y que este número puede ser impar.
"""
c=1
Alumnos=[]
Edad=[]


n=int(input("Ingrese el numero de alumnos:"))
if n%2!=0:
   for i in range(0,n,1):
    print("Alumno No.",c,end=" ")
    alumno=str(input("Ingrese el nombre del alumno:"))
    print("Alumno No.",c,end=" ")
    edad=float(input("Ingrese la edad del alumno:"))
    Alumnos.append(alumno)
    Edad.append(edad)
    c=c+1
    
else:
   print("Intenete con otro numero ...")
if n%2!=0:
 Union=list(zip(Alumnos, Edad))
 Vmax=max(Union, key=lambda item: item[1])
 print("El alumno con mayor edad es",Vmax[0], "con una edad de",Vmax[1],"años")