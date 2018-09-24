step = 1
path = str()
secret = str('SSNWES')

while step < 30:
    move = input("You are in the magic maze. Which way to go? (N,S,E,W)")
    if move == "N":
        path = path + "N"
    elif move == "S":
        path = path + "S"
    elif move == "E":
        path = path + "E"
    elif move == "W":
        path = path + "W"  # why if I use “or” and“and” doesnt work?
    else:
        print("Please enter direction of your moves with the right command:N[orth], S[outh], E[ast] and W[est]. ")

    print("This the path u have walked", path)
    step = step + 1

    if step == 6 :
        if path == secret:
            print("You have escaped the maze in ", step, " moves ")
            break
        else:
            path = str()
            print("Path got reset")

    elif step == 12:
        if path == secret:
            print("You have escaped the maze in ", step, " moves ")
            break
        else:
            path = str()
            print("Path got reset")

    elif step == 18:
        if path == secret:
            print("You have escaped the maze in ", step, " moves ")
            break
        else:
            path = str()
            print("Path got reset")

    elif step == 24:
        if path == secret:
            print("You have escaped the maze in ", step, " moves ")
            break
        else:
            path = str()
            print("Path got reset")


    if step == 10:
        print("You have lost one life(you have moved 10 moves)")
    if step == 20:
        print("You have lost one life(you have moved 10 moves)")
    elif step == 30:  # WAIT
        print("You lost 3 lives, too bad, you are dead.")
        print("GAME OVER")
        break

    print("This the path u have walked", path)