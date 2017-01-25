'''
A simple finite state machine
Author:Kay(github.com/kayhe)
'''
from myhdl import *

states = enum('UP', 'DOWN', 'GOINGUP','GOINGDOWN','STOP')
def fsm(state,stopFlag,clk,reset):
    upcontrol = Signal(bool(0))
    downcontrol = Signal(bool(0))

    @always_seq(clk.posedge,reset=reset)
    def logic():
        if state == states.STOP:
            pass
        elif state == states.UP or state == states.DOWN:
            upcontrol.next = 0
            downcontrol.next = 0
            state.next = states.STOP
        elif state == states.GOINGUP:
            upcontrol.next = 1
            downcontrol.next = 0
            if stopFlag:
                state.next = states.UP
        elif state == states.GOINGDOWN:
            upcontrol.next = 0
            downcontrol.next = 1
            if stopFlag:
                state.next = states.DOWN
        else:
            raise ValueError("Check your state, mate")
        
    return logic
