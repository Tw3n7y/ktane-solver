import math

red = 0
blue = 0
black = 0
def strsplit(s):
    return [char for char in s]
def wires(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    wire_amount = int(input("wire amount:"))
    if  wire_amount == 3:
        red_wires = int(input("red wires:"))
        if red_wires == 0:
            print("cut wire 2")
        else:
            last_wire_white = input("is the last wire white? [y/n]")
            if last_wire_white == "y":
                print("cut wire 3")
            else:
                blue_wires = int(input("blue wires:"))
                if blue_wires > 1:
                    print("cut the last blue wire")
                else:
                    print("cut wire 3")
    elif wire_amount == 4:
        x = int(serial[5])
        red_wires = int(input("red wires:"))
        if x % 2 == 1 and red_wires > 1:
            print("cut wire 4")
        else:
            last_wire_yellow = input("is the last wire yellow? [y/n]")
            if last_wire_yellow == "y" and red_wires == 0:
                print("cut wire 1")
            else:
                blue_wires = int(input("blue wires:"))
                if blue_wires  == 1:
                    print("cut wire 1")
                else:
                    yellow_wires = int(input("yellow wires:"))
                    if yellow_wires > 1:
                        print("cut wire 4")
                    else:
                        print("cut wire 2")
    elif wire_amount == 5:
        x = int(serial[5])
        last_wire_black = input("is the last wire black? [y/n]")
        if x % 2 == 1 and last_wire_black == "y":
            print("cut wire 4")
        else:
            red_wires = int(input("red wires:"))
            yellow_wires = int(input("yellow wires:"))
            if red_wires == 1 and yellow_wires > 1:
                print("cut wire 1")
            else:
                black_wires = int(input("black wires:"))
                if black_wires != 0:
                    print("cut wire 2")
                else:
                    print("cut wire 1")
    elif wire_amount == 6:
        yellow_wires = int(input("yellow wires:"))
        x = int(serial[5])
        if yellow_wires == 0 and x % 2 == 1:
            print("cut wire 3")
        else:
            white_wires = int(input("white wires:"))
            if white_wires > 1 and yellow_wires == 1:
                print("cut wire 4")
            else:
                red_wires = int(input("red wires:"))
                if red_wires == 0:
                    print("cut wire 6")
                else:
                    print("cut wire 4")

def wire_sequence(name):
    for x in range(9):
        wire = input("input wire colour and destination with format '[colour initial][destination]' and 'w' for black:")
        wire = split(wire)
        if wire[0] == "r":
            red = red + 1
        elif wire[0] == "b":
            blue = blue +  1
        elif wire[0] == "w":
            black = black + 1
        else:
            print("invalid")
        if wire[0] == "r":
            if red == 1 and wire[1] == "c":
                print("cut")
            elif red == 2 and wire[1] == "b":
                print("cut")
            elif red == 3 and wire[1] ==  "a":
                print("cut")
            elif red == 4 and wire[1] != "b":
                print("cut")
            elif red == 5 and wire[1] == "b":
                print("cut")
            elif red == 6 and wire[1] != "b":
                print("cut")
            elif red == 7:
                print("cut")
            elif red == 8 and wire[1] != "c":
                print("cut")
            elif red == 9 and  wire[1] == "b":
                print("cut")
            else:
                print("ignore")
        elif wire[0] == "b":
            if blue == 1 and wire[1] == "b":
                print("cut")
            elif blue ==  2 and wire[1] != "b":
                print("cut")
            elif blue == 3 and wire[1] == "b":
                print("cut")
            elif blue ==  4 and wire[1] == "a":
                print("cut")
            elif blue == 5 and wire[1] ==  "b":
                print("cut")
            elif blue == 6 and wire[1] != "a":
                print("cut")
            elif blue == 7 and wire[1] == "c":
                print("cut")
            elif blue == 8 and wire[1] != "b":
                print("cut")
            elif blue == 9 and wire[1] == "a":
                print("cut")
            else:
                print("ignore")
        elif wire[0] == "w":
            if black == 1:
                print("cut")
            elif black == 2 and wire[1] != "b":
                print("cut")
            elif black == 3 and wire[1] == "b":
                print("cut")
            elif black == 4 and wire[1] != "b":
                print("cut")
            elif black == 5 and wire[1] == "b":
                print("cut")
            elif black == 6 and wire[1] != "a":
                print("cut")
            elif black == 7 and wire[1] != "c":
                print("cut")
            elif black == 8 and wire[1] == "c":
                print("cut")
            elif black == 9 and wire[1] == "c":
                print("cut")
            else:
                print("ignore")
    
    
def complicated_wires(name):
    wire_amount = int(input("wire amount:"))
    for x in range(wire_amount):
        wire_colours = input("wire colours:")
        strsplit(wire_colours)
        star = input("star? [y/n]:")
        led = input("LED? [y/n]:")
        x = int(serial[5])
        if (("r" in wire_colours and "b" in wire_colours and star != "y" and led != "y") or ("r" in wire_colours and not ("b" in wire_colours) and led != "y" and star != "y") or ("b" in wire_colours and not ("r" in wire_colours) and led != "y" and star != "y") or ("r" in wire_colours and "b" in wire_colours and led == "y" and star != "y")   and x % 2 == 0) or (not ("b" in wire_colours) and not ("r" in wire_colours) and led != "y" and star != "y") or (star == "y" and led != "y" and not ("b" in wire_colours)) or (("b" in wire_colours  and not ("r" in wire_colours) and star != "y" and led == "y") or ("b" in wire_colours and "r" in wire_colours and star == "y" and led != "y") or ("b" in wire_colours and not ("r" in wire_colours) and star == "y" and led == "y") and parallel_ports > 0) or ((not ("b" in wire_colours) and led == "y") and batteries > 2):
            print("cut")
        else:
            print("ignore")
