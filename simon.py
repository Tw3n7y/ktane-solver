def simonsays(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    strikes = int(input("strikes:"))
    vowels = ["a", "e", "i", "o", "u"]
    for char in serial:
        if char in vowels:
            if strikes == 0:
                print("r=b, b=r, g=y, y=g")
            elif strikes == 1:
                print("r=y, b=g, g=b, y=r")
            elif strikes > 1:
                print("r=g, b=r, g=y, y=b")
                break
    if strikes == 0:
        print("r=b, b=y, g=g, y=r")
    elif strikes == 1:
        print("r=r, b=b, g=y, y=g")
    elif strikes > 1:
        print("r = y, b=g, g=b, y=r")
