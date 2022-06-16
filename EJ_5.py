# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:47:48 2022

@author: CrIva
"""
"""
Realice un algoritmo que lea dos vectores de cien elementos y que calcule la suma de éstos guardando 
su resultado en otro vector, el cual se debe presentar en forma impresa
"""


# Nombre_vector=[] para crear un vector vacio,se utila para despues ingresarle datos que pidamos
A=[]
B=[]
C=[]
n=101#101 ya que range se detiene un dato antes del especificado es decir en el numero 100
n1=100
# Este ciclo sirve para que podamos ingresar los elementos del vector A y B  segun el tamaño 
# que hallamos elegido, el ciclo empieza en 1 a n(tamaño del vector), con un paso a 1
for i in range(1,n,1): #se cuenta desde uno para omiter el 0
 A.append(i)
 B.append(i)

# Para poder sumar los elementos respectivos del Vector A y el B utilizamos el vector C
# el cual sigue vacio , utilizamos C.append para ingresar los resultados de la suma con
# (A[i]+B[i]), en este caso el ciclo realiza la suma de los elementos desde o hasta n 
for i in range(0,n1,1):#en este caso se busca la suma de cada elemento,por lo tanto solamente designamos desde
#donde se empieza hasta donde termina,  lo que el rango es de 0 a 99 lo es igual a 100 elemntos yas que el 0
# tambien se cuenta como posicion de un elemento
 C.append( A[i] + B[i] )
  
print("El vector A es:",A,end = "\n\n")
print("El vector B es:",B,end = "\n\n")
print("El vector C es la suma de los vectores A y B es:",C,end = "\n")

    
