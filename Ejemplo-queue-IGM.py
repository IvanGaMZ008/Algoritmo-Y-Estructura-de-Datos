# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:20:36 2022

@author: CrIva
"""

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
input_queue = Queue()

input_queue.enqueue('DOWN')
input_queue.enqueue('RIGHT')
input_queue.enqueue('B')

key_pressed = input_queue.dequeue() 

key_pressed = input_queue.dequeue()

key_pressed = input_queue.dequeue()
