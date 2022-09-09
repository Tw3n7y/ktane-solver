def morse(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    letter1 = input("first letter [. for short, - for long]:")
    letter2 = input("second letter [. for short, - for long]:")
    letter3 = input("third letter [. for short, - for long]:")
    if letter1 == "...":
        if letter2 == "....":
            print("3.505") #shell
        elif letter2 == ".-..":
            print("3.522") #slick
        elif letter2 == "-":
            if letter3 == ".-.":
                print("3.545") #strobe
            elif letter3 == ".":
                print("3.582") #steak
            elif letter3 == "..":
                print("3.592") #sting
    elif letter1 == "....":
        print("3.515") #halls
    elif letter1 == "-":
        print("3.532") #trick
    elif letter1 == "-...":
        if letter2 == "---":
            if letter3 == "-..-":
                print("3.535") #boxes
            elif letter3 == "--":
                print("3.565") #bombs
        elif letter2 == "..":
            print("3.552") #bistro
        elif letter2 == ".-.":
            if letter3 == ".":
                print("3.572") #break
            elif letter3 == "..":
                print("3.575") #brick
        elif letter2 == ".":
            print("3.600")
    elif letter1 == ".-..":
        print("3.542")
    elif letter1 == "..-.":
        print("3.555")
    elif letter1 == "...-":
        print("3.595")
    
