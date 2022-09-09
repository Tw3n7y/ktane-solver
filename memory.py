def memory(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    display = int(input("display:"))
    if display == 1:
        label1 = input("position 2" + "\n" + "input label of position 2:")
        position1 = 2
    elif display == 2:
        label1 = input("position 2" + "\n" + "input label of position 2:")
        position1 = 2
    elif display == 3:
        label1 = input("position 3" + "\n" + "input label of position 3:")
        position1 = 3
    elif display == 4:
        label1 = input("position 4" + "\n" + "input label of position 4:")
        position1 = 4
    display = int(input("display:"))
    if display  == 1:
        position2 =  "position" +  input("label 4" + "\n" + "input position of label 4:")
        label2 = 4
    elif display == 2:
        print("position")
        print(position1)
        label2 = input("input:")
        position2 = position1
    elif display == 3:
        label2 = input("position 1" + "\n" + "input label of position 1:")
        position2 = 1
    elif display == 4:
        print("position")
        print(position1)
        label2 = input("input:")
        position2 = position1
    display = int(input("display:"))
    if display == 1:
        print("label")
        print(label2)
        position3 = input("input:")
        label3 = label2
    elif display == 2:
        print("label")
        print(label1)
        position3 = input("input:")
        label3 = label1
    elif display == 3:
        label3 = input("position 3" + "\n" + "input label of position 3:")
        position3 = "position 3:"
    elif display == 4:
        position3 = input("label 4" + "\n" + "input position of label 4:")
        label3 = 4
    display = int(input("display:"))
    if display == 1:
        print("position")
        print(position1)
        label4 = input("input:")
        position4 = position1
    elif display == 2:
        label4 = input("position 1" + "\n" + "input label of position 1:")
        position4 = 1
    elif display == 3:
        print("position")
        print(position2)
        label4 = input("input:")
        position4 = position2
    elif display == 4:
        print("position")
        print(position2)
        label4 = input("input:")
        position4 = position2
    display = int(input("display:"))
    if display == 1:
        print("label")
        print(label1)
    elif display == 2:
        print("label")
        print(label2)
    elif display == 3:
        print("label")
        print(label4)
    elif display == 4:
        print("label")
        print(label3)
