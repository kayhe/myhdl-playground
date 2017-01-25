'''
Testbench for the simple finite state machine
Author:Kay(github.com/kayhe)
'''
from myhdl import *
from module import * 

def simulator():
    curr_state = Signal(states.GOINGUP)
    stopFlag = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(1,active=False,async=True) 

    themachine = fsm(curr_state,stopFlag,clk,reset)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def generator():
        for i in range(4):
            yield clk.posedge
        stopFlag.next = 1
        for i in range(3):
            yield clk.posedge
        stopFlag.next = 0
        curr_state.next = states.GOINGDOWN
        for i in range(4):
            yield clk.posedge
        stopFlag.next = 1
        for i in range(3):
            yield clk.posedge
        raise StopSimulation

    return themachine, clkgen, generator


test_fsm = traceSignals(simulator)
sim = Simulation(test_fsm)
sim.run()
