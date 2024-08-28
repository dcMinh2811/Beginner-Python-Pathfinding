Robot_Pos = [13,6]
Goal_Pos = [7,3]
Wall_Pos = [[12, 6], [12, 5], [13, 5], [14, 5]]
Checked = [Robot_Pos.copy()]

def moveHandler(x,y):
    return [Robot_Pos[0] + x, Robot_Pos[1] + y]

def left():
    return moveHandler(-1,0)

def right():
    return moveHandler(1,0)

def forward():
    return moveHandler(0,1)

def backward():
    return moveHandler(0,-1)

all_moves = [left, right, forward, backward]
    
def checkAvailable():
    global Robot_Pos
    original_Pos = Robot_Pos.copy()
    neighbours = []
    
    for move in all_moves:
        new_pos = move()
        if new_pos not in Wall_Pos and new_pos not in Checked:
            neighbours.append(new_pos)
        Robot_Pos = original_Pos.copy()

    return neighbours

count = 1
def step():
    global count, Robot_Pos, Goal_Pos
    currentBest = [float('inf'),None]
    Possible_moves = checkAvailable()
    print("\n\nPossible moves now:",Possible_moves)
    for move in Possible_moves:
        dist = abs(move[0]-Goal_Pos[0])+abs(move[1]-Goal_Pos[1])
        if dist < currentBest[0]:
            currentBest[0] = dist
            currentBest[1] = move

    if currentBest[1]:
        Robot_Pos = currentBest[1]
        Checked.append(currentBest[1].copy())
    else:
        print("No move found")
    print("Currents:",currentBest)
    return Checked[-1]

while Robot_Pos != Goal_Pos:
    if len(checkAvailable()) > 0:
        print("Robot chose position:",step(),"\nCount:",count)
        print("Checked",Checked)
    else:
        print("No way to go")
        break
    count += 1
