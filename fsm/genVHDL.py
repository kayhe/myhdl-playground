'''
VHDL code generation
Author:Kay(github.com/kayhe)
'''
from myhdl import toVHDL, Signal, ResetSignal
from module import *

state = Signal(states.GOINGUP)
stopFlag = Signal(bool(0))
clk = Signal(bool(0))
reset = ResetSignal(1,active=False,async=True)
fsm_inst = toVHDL(fsm,state,stopFlag,clk,reset)
