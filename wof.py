def wof(serial, lit_ind_amount, unlit_ind_amount, d_batteries, aa_batteries, battery_holders, parallel_ports, dvi_d_ports, rj_45_ports, serial_ports, stereo_rca_ports, lit_inds, unlit_inds):
    for x in range(3):
        display_word = input("input '0' for a blank display. display_word:")
        if display_word ==  "yes" or display_word ==  "led" or display_word ==  "nothing" or display_word ==  "they  are":
            solve_word = input("word in mid-left:")
        elif display_word ==  "first" or display_word ==  "okay" or  display_word ==  "c":
            solve_word = input("word in top-right:")
        elif display_word == "display" or display_word ==  "says" or display_word ==  "you are" or display_word ==  "hold on" or display_word ==  "cee" or display_word ==  "there":
            solve_word = input("word in  bottom-right:")
        elif display_word == "0" or display_word ==  "reed"  or display_word ==  "leed"  or display_word ==  "they're":
            solve_word = input("word  in bottom-left:")
        elif display_word == "blank" or display_word ==  "read" or  display_word ==  "their" or  display_word ==  "red" or display_word ==  "you" or display_word ==  "your" or display_word ==  "you're":
            solve_word = input("word in mid-right:")
        else:
            solve_word  = input("word in top-left:")
        if solve_word == "ready":
            print("YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY")
        elif solve_word == "first":
            print("LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST")
        elif solve_word == "no":
            print("BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO")
        elif solve_word == "blank":
            print("WAIT, RIGHT, OKAY, MIDDLE, BLANK")
        elif solve_word == "nothing":
            print("UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING")
        elif solve_word == "yes":
            print("OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES")
        elif solve_word == "what":
            print("UHHH, WHAT")
        elif solve_word == "uhhh":
            print("READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH")
        elif solve_word  == "left":
            print("RIGHT, LEFT")
        elif solve_word ==  "right":
            print("YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT")
        elif solve_word == "middle":
            print("BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE")
        elif solve_word == "okay":
            print("MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY")
        elif solve_word == "wait":
            print("UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT")
        elif solve_word == "press":
            print("RIGHT, MIDDLE, YES, READY, PRESS")
        elif solve_word == "you":
            print("SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU")
        elif solve_word == "you are":
            print("YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE")
        elif solve_word == "your":
            print("UH UH, YOU ARE, UH HUH, YOUR")
        elif solve_word == "you're":
            print("YOU, YOU'RE")
        elif solve_word == "ur":
            print("DONE, U, UR")
        elif solve_word ==  "u":
            print("UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U")
        elif solve_word == "uh huh":
            print("UH HUH")
        elif solve_word == "uh uh":
            print("UR, U, YOU ARE, YOU'RE, NEXT, UH UH")
        elif solve_word == "what?":
            print("YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?")
        elif solve_word == "done":
            print("SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE")
        elif solve_word == "next":
            print("WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT")
        elif solve_word == "hold":
            print("YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD")
        elif solve_word == "sure":
            print("YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE")
        elif solve_word == "like":
            print("YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE")
