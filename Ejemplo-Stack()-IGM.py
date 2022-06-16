# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:53:16 2022

@author: CrIva
"""

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
    
document_actions = Stack()

# The first enters the title of the document
document_actions.push('action: enter; text_id: 1; text: This is my favourite document')
# Next they center the text
document_actions.push('action: format; text_id: 1; alignment: center')
# As with most writers, the user is unhappy with the first draft and undoes the center alignment
document_actions.pop()
# The title is better on the left with bold font
document_actions.push('action: format; text_id: 1; style: bold')