# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:30:32 2022

@author: CrIva
"""
"""
ENUNCIADO DEL PROBLEMA 3
Lea un vector y a partir de él forme un segundo vector, de tal forma que el primer elemento pase a ser 
el segundo, el segundo pase a ser el tercero, el último pase a ser el primero, y  así sucesivamente. 
"""

A=[]
n=int(input("Ingrese el tamano del vector:"))

for i in range(0,n,1):
 elemento=int(input("Ingresa un numero:")) 
 A.append(elemento)
 
print(sep=" ")
print("El vector original es el siguiente",A)#mostramos el Vector A antes de crear otro Vector
B=A #Asignamos el segundo vector con los elementos del primero
print(sep="\n")
B.insert(0,B.pop()) #Para agregar un elemento al principio del vector use insert(posición, "nuevo elemento") 
# se establece el primer argumento como 0, que denota que la inserción se realiza en el índice 0(inicio de la
# lista),despues use la funcion pop() la cual elimina y devuelve el último elemento de la lista, de esta
# manera se recorre cada elemento a una posicion mas de la original

print("El vector modificado es el siguiente",B)#Ahora el vector B ya esta modificado
