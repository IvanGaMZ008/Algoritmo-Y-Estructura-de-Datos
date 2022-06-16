# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:54:04 2022

@author: CrIva
"""
"""
5.Crea una pila llamada NombresDePerros que comience vacía, y llénala con instrucciones 
en el código. Una vez completada imprimirla en pantalla
"""
NombresDePerros=[]
N=int(input("Ingres el numero de nombres de perro@s:"))
for i in range (0,N,1):
    p=str(input("Ingresa el nombe del perr@:"))
    NombresDePerros.append(p)
    
print(NombresDePerros)
