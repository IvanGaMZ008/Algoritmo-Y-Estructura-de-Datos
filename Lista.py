# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:56:15 2022

@author: CrIva
"""
"""
6. Escribir un código en el cual se comience una lista de 6 elementos y se le pregunte al usuario 
el tratamiento que se le quiera dar. Si el usuario ingresa “pila“, se deberán eliminar y mostrar uno
a uno en el orden convencional de lapila. Hacer lo mismo pero en el orden de la cola para el caso 
que se ingrese “cola”.
"""

A=["Juan","Selena","Vicente","Jose","Michael","Luis"]
n=0
n1=0
print("¿Que desea realizarle a la lista?")
print("Escriba la estrutura de datos que desea ya sea bien cola o pila")
Option=str(input("Opcion:"))
print(A)

if Option=="cola":
    for i in range(0,len(A),1):
     print(A.pop(0))
     
elif Option=="pila":
 for i in range(0,6,1):
   print(A.pop())
else:
 print("Intente de nuevo")
