def maze(name):
    global maze
    global player
    global goal
    circle = input("coords of any circle:")
    player = input("player coords:")
    goal = input("goal coords:").split(",")
    if circle == "1,5" or circle == "6,4":
        maze = [
            ["ur", "rl", "dl", "rd", "rl", "l"], #urdl
            ["ud", "rd", "ul", "ur", "rl", "dl"],
            ["ud", "ur", "dl", "rd", "rl", "udl"],
            ["ud", "r", "url", "ul", "r", "udl"],
            ["urd", "rl", "dl", "rd", "l", "ud"],
            ["ur", "l", "ur", "ul", "r", "ul"]]
    elif circle == "2,3" or circle == "5,5":
        maze = [
            ["r", "rdl", "l", "rd", "rdl", "l"],
            ["rd", "ul", "rd", "ul", "ur", "dl"],
            ["ud", "rd", "ur", "rd", "rl", "udl"],
            ["urd", "ul", "dl", "ul", "d", "ud"],
            ["ud", "d", "ud", "rd", "ul", "ud"],
            ["u", "ur", "ul", "ur", "rl", "ul"]]

def checksquare(x,y):
    travelLog = []
    if [x,y] in travelLog:
        return ""
    travelLog.appgoal([x,y])
    if [str(x),",",str(y)] == goal:
        return "dump"
    if "u" in maze[y][x]:
        up = checksquare(x,y-1)
        if up == "dump":
            return "u"
        if len(up) > 0:
            return "u" + up
    if "r" in maze[y][x]:
        right = checksquare(x+1,y)
        if right == "dump":
            return "r"
        if len(right) > 0:
            return "r" + right
    if "d" in maze[y][x]:
        down = checksquare(x,y+1)
        if down == "dump":
            return "d"
        if len(down) > 0:
            return "d" + down
    if "l" in maze[y][x]:
        left = checksquare(x-1,y)
        if left == "dump":
            return "l"
        if len(left) > 0:
            return "l" + left
    return ""
    print(checksquare(int(player[0]),int(player[2])))
    

