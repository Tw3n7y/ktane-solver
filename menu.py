import math
import argparse
import wires
import wof
import memory
import button
import keypad
import morse
import simon
import password
import maze
lit_ind_check = 0
unlit_ind_check = 0
lit_inds = []
unlit_inds = []

def strsplit(s):
    return [char for char in s]


def lit_ind():
    if lit_ind_check != lit_ind_amount:
        lit_ind_add()

def lit_ind_add():
    global lit_ind_check
    global lit_inds
    lit_inds.append(input("lit indicator:"))
    lit_ind_check = lit_ind_check + 1
    print(lit_ind_check)
    lit_ind()

def unlit_ind():
    if  unlit_ind_check != unlit_ind_amount:
        unlit_ind_add()

def unlit_ind_add():
    global unlit_inds
    global unlit_ind_check
    unlit_inds.append(input("unlit indicator:"))
    unlit_ind_check = unlit_ind_check + 1
    unlit_ind()



serial = input("serial:")
serial = strsplit(serial)
lit_ind_amount = int(input("lit indicator amount:"))
unlit_ind_amount = int(input("unlit indicator amount:"))
d_batteries =  int(input("d battery amount:"))
aa_batteries = int(input("aa battery amount:"))
battery_holders =  int(input("battery holders:"))
parallel_ports = int(input("parallel ports:"))
dvi_d_ports = int(input("dvi-d ports:"))
ps_2_ports =  int(input("ps/2 ports:"))
rj_45_ports = int(input("rj-45 ports:"))
serial_ports = int(input("serial ports:"))
stereo_rca_ports = int(input("stereo rca ports:"))
batteries = d_batteries + aa_batteries
lit_ind()
unlit_ind()

modules = {
 "wires": wires.wires,
 "sequence": wires.wire_sequence,
 "cwires": wires.complicated_wires,

 "memory": memory.memory,
 
 "button": button.button,
 "sbutton": button.sbutton,
 
 "wof": wof.wof,

 "maze": maze.maze,

 "keypad": keypad.keypad,
 "rkeypad": keypad.round_keypad,

 "morse": morse.morse,

 "simon": simon.simonsays,

 "password": password.password
}

def run_module(module):
    global serial
    if module in modules:
        print(f"Executing module {module}")
        function = modules[module]
        function(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds)
    else:
        print(f"Module {module} unknown!")

while True:
    run_module(input("Enter module name: "))
