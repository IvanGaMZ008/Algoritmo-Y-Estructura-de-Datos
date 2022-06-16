# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:30:43 2022

@author: CrIva
"""
"""
Este código de ejemplo, muestra la entrada de valores a la cola FIFO y la salida de la misma.
"""
import queue
import random
import sys
 
queue_time = queue.Queue()
 
print("Guardando elementos en la cola...")
for i in range (5):
    random_time = random.randint(1, 100)
    queue_time.put(random_time)
    print("Numero %d agregado a la cola" % random_time)
 
print("Leyendo elementos de la cola...")
while True:
    if queue_time.empty() == False:
        time_read = queue_time.get()
        print("Numero %d leido de la cola" % time_read)
    else:
        print("La cola esta vacia!!")
        break