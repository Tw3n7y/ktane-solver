def knob(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    ident = input("identifying four [u for unlit, l for lit]:")
    if ident == "ulul" or ident == "ullu":
        print("up")
    elif ident == "uulu" or ident == "uluu":
        print("down")
    elif ident == "ulll":
        print("left")
    elif ident == "llul" or ident == "lulu":
        print("right")
    else:
        print("invalid")
