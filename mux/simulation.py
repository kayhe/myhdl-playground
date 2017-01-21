'''
Simulation and VHDL code generation for the multiplexer
Author:Kay(github.com/kayhe)
'''
from myhdl import *
from module import Mux
from random import randrange

def test_mux():
    a,b,s,y,clk = [Signal(bool(0)) for i in range(5)]

    mux_inst = Mux(a,b,s,y)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.negedge)
    def randomize():
        a.next = randrange(2)
        b.next = randrange(2)
        s.next = randrange(2)

    return mux_inst, clkgen, randomize

def simulator(timestep):
    tb = traceSignals(test_mux)
    sim = Simulation(tb)
    sim.run(timestep)

def emitVHDL():
    a,b,s,y,clk = [Signal(bool(0)) for i in range(5)]
    toVHDL(Mux,a,b,s,y)

simulator(1000)
emitVHDL()
