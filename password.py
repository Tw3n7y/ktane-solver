def strsplit(s):
    return [char for char in s]

def password(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    column1 = strsplit(input("first column:"))
    column2 = strsplit(input("second column:"))
    column3 = strsplit(input("third column:"))
    passes = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]
    newpasses = []
    for item in passes:
        for letter in column1:
            if letter == item[0]:
                newpasses.append(item)
        if item in newpasses:
            newpasses.remove(item)
            for letter in column2:
                if letter == item[1]:
                    newpasses.append(item)
        if item in newpasses:
            newpasses.remove(item)
            for letter in column3:
                if letter == item[2]:
                    newpasses.append(item)
    print(newpasses)
