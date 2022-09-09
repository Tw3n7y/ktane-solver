def keypad(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    print("a - Copyright sign\nb - Black star\nc - White star\nd - Smiley with 2 eyes\ne - Reflecting K (>K)\nf - Omega\ng - 4-legged animal\nh - Curvy w with eye and eye brow\ni - Cursive small H\nj - Underlined x\nk - Flat 6\nl - Zig zag\nm - A with a line connected below it (looks like 3 legs, do not be fooled)\nn - ae\no - Partially written 3\np - Backwards curved E with eyes\nq - Ring of half circles\nr - Backwards N with phone above it\ns - 3 with antennae and a tail\nt - Rotated question mark\nu - Backwards stylish P\nv - C with dot in center\nw - Backwards C with dot in center\nx - Trident\ny - 3 legged thing connecting to single point on triangle (not A)\nz - Loop de loop\n0 - 2 lines with 1 perpendicular crossing\n1 - O with a line connected below it\n2 - Zeta (rotated curvy 2)\n3 - Lambda (rotated y with line)\n4 - t and b combined")
    symbol1 = input("input symbol 1:")
    symbol2 = input("input symbol 2:")
    symbol3 = input("input symbol 3:")
    symbol4 = input("input symbol 4:")
    symbols = [symbol1, symbol2, symbol3, symbol4]
    columns = [["1", "m", "3", "l", "g" , "i", "w"],
    ["p", "1", "w",  "z", "c", "i", "t"],
    ["a", "h", "z", "e", "o", "3", "c"],
    ["k", "u", "4", "g", "e", "t", "d"],
    ["x", "d", "4", "w", "u", "s", "b"],
    ["k", "p", "0", "n", "x", "r", "f"]]
    for column1 in columns:
        if symbol1 in column1 and symbol2 in column1 and symbol3 in column1 and symbol4 in column1:
            for item in column1:
                if item in symbols:
                    print(item)
#"a - Copyright sign\nb - Black star\nc - White star\nd - Smiley with 2 eyes\ne - Reflecting K (>K)\nf - Omega\ng - 4-legged animal\nh - Curvy w with eye and eye brow\ni - Cursive small H\nj - Underlined x\nk - Flat 6\nl - Zig zag\nm - A with a line connected below it (looks like 3 legs, do not be fooled)\nn - ae\no - Partially written 3\np - Backwards curved E with eyes\nq - Ring of half circles\nr - Backwards N with phone above it\ns - 3 with antennae and a tail\nt - Rotated question mark\nu - Backwards stylish P\nv - C with dot in center\nw - Backwards C with dot in center\nx - Trident\ny - 3 legged thing connecting to single point on triangle (not A)\nz - Loop de loop\n0 - 2 lines with 1 perpendicular crossing\n1 - O with a line connected below it\n2 - Zeta (rotated curvy 2)\n3 - Lambda (rotated y with line)\n4 - t and b combined"
def strsplit(s):
    return [char for char in s]

def round_keypad(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    print("a - Copyright sign\nb - Black star\nc - White star\nd - Smiley with 2 eyes\ne - Reflecting K (>K)\nf - Omega\ng - 4-legged animal\nh - Curvy w with eye and eye brow\ni - Cursive small H\nj - Underlined x\nk - Flat 6\nl - Zig zag\nm - A with a line connected below it (looks like 3 legs, do not be fooled)\nn - ae\no - Partially written 3\np - Backwards curved E with eyes\nq - Ring of half circles\nr - Backwards N with phone above it\ns - 3 with antennae and a tail\nt - Rotated question mark\nu - Backwards stylish P\nv - C with dot in center\nw - Backwards C with dot in center\nx - Trident\ny - 3 legged thing connecting to single point on triangle (not A)\nz - Loop de loop\n0 - 2 lines with 1 perpendicular crossing\n1 - O with a line connected below it\n2 - Zeta (rotated curvy 2)\n3 - Lambda (rotated y with line)\n4 - t and b combined")
    symbols = input("symbols:")
    strsplit(symbols)
    columns = [["1", "m", "3", "l", "g" , "i", "w"],
    ["p", "1", "w",  "z", "c", "i", "t"],
    ["a", "h", "z", "e", "o", "3", "c"],
    ["k", "u", "4", "g", "e", "t", "d"],
    ["x", "d", "4", "w", "u", "s", "b"],
    ["k", "p", "0", "n", "x", "r", "f"]]
    matches = [0, 1, 2, 3, 4, 5]
    temp = -1
    for x in range(6):
        for symbol in symbols:
            if symbol in columns[x]:
                matches[x] +=6
        if matches[x] > temp:
            temp = matches[x]
            valid = x
    for x in range(8):
        if not symbols[x] in columns[valid]:
            print (symbols[x])

    
