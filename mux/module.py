'''
Logical description of the multiplexer
Author:Kay(github.com/kayhe)
'''
from myhdl import *

def Mux(a,b,s,y):
    
    @always_comb
    def logic():
        if s == 0:
            y.next = a
        else:
            y.next = b

    return logic
