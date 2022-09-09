def button(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    global batteries
    global lit_ind
    word = input("button word:")
    colour = input("button colour:")
    if word == "abort" and colour == "blue":
        print("hold the button \n if the strip is blue, 4 in any position \n if white, 1 in any position \n if yellow, 5 in any position \n if other, 1 in any position")
    elif batteries > 1 and word == "detonate":
        print("press and immediately release")
    elif "car" in lit_inds and colour == "white":
        print("hold the button \n if the strip is blue, 4 in any position \n if white, 1 in any position \n if yellow, 5 in any position \n if other, 1 in any position")
    elif "frk" in lit_inds and batteries > 2:
        print("press and immediately release")
    elif colour == "yellow":
        print("hold the button \n if the strip is blue, 4 in any position \n if white, 1 in any position \n if yellow, 5 in any position \n if other, 1 in any position")
    elif colour == "red" and word == "hold":
        print("press and immediately release")
    else:
        print("hold the button \n if the strip is blue, 4 in any position \n if white, 1 in any position \n if yellow, 5 in any position \n if other, 1 in any position")

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def strsplit(s):
    return [char for char in s]

def sbutton(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    colour = input("colour")
    label = input("label (input 'none' if label missing):")
    vowels = ["a", "e", "i", "o", "u"]
    y_b = ["yellow", "blue"]
    dark_grey = ["dark_grey", "dark_gray"]
    for char in serial:
        if char in vowels:
            s_vowel = True
    if label == "none":
        label == ""
    strsplit(label)
    greatest = -1
    for char in serial:
        if isint(char):
            if int(char) > greatest:
                greatest = int(char)
    if colour == "blue" and aa_batteries > d_batteries:
        print("""hold the button
If LED is static:
Cyan: Release when the two seconds digits add up to 7.
Orange: Release when the two seconds digits add up to 3 or 13.
Other: Release when the two seconds digits add up to 5.
If the LED is flickering, follow these rules instead:
Cyan: Release when the number of seconds remaining is a multiple of 7.
Orange: Release when the number of seconds displayed is either prime or 0.
Other: Release one second after the two seconds digits add up to a multiple of 4.""")
    elif colour in y_b and greatest >= len(label):
        print("press and immediately release")
    elif colour in y_b and label in ["purple", "jade", "maroon", "indigo"]:
        print("""hold the button
If LED is static:
Cyan: Release when the two seconds digits add up to 7.
Orange: Release when the two seconds digits add up to 3 or 13.
Other: Release when the two seconds digits add up to 5.
If the LED is flickering, follow these rules instead:
Cyan: Release when the number of seconds remaining is a multiple of 7.
Orange: Release when the number of seconds displayed is either prime or 0.
Other: Release one second after the two seconds digits add up to a multiple of 4.""")
    elif label == "none":
        print("press and immediately release when the two seconds digits on the timer match")
    elif not colour in dark_grey and len(label) < lit_ind_amount:
        print("press and immediately release")
    elif unlit_ind_amount >= 2 and s_vowel:
        print("press and immediately release")
    else:
        print("""hold the button
If LED is static:
Cyan: Release when the two seconds digits add up to 7.
Orange: Release when the two seconds digits add up to 3 or 13.
Other: Release when the two seconds digits add up to 5.
If the LED is flickering, follow these rules instead:
Cyan: Release when the number of seconds remaining is a multiple of 7.
Orange: Release when the number of seconds displayed is either prime or 0.
Other: Release one second after the two seconds digits add up to a multiple of 4.""")
