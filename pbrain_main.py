import sys
import pbrain_misc as misc
import pbrain_ai as ai

MIN_BOARD = 5
MAX_BOARD = 100
COMMANDS_STR = [ "START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT" ]
FUNCTIONS_STR = [ "startCmd", "turnCmd", "beginCmd", "boardCmd", "infoCmd", "endCmd", "aboutCmd" ]
ABOUT = 'name="VeryMuchSmartIA", version="1.0", author="samuel.rousseaux@epitech.eu", country="France"'

boardSize = 0
gameBoard = None

def startCmd(size, unused):
    global boardSize
    global gameBoard

    size = int(size)
    if size < MIN_BOARD or size > MAX_BOARD:
        misc.printToProgram("ERROR message - Given size is {} but must be >= {} and <= {}".format(size, MIN_BOARD, MAX_BOARD))
        sys.exit(84)
    
    boardSize = size
    gameBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
    misc.printToProgram("OK")

def turnCmd(pos, unused):
    global gameBoard
    global boardSize

    posTab = pos.split(",")
    gameBoard[int(posTab[1])][int(posTab[0])] = 2

    pos = ai.chooseNextMove(gameBoard)
    gameBoard[pos[0]][pos[1]] = 1
    misc.printToProgram("{},{}".format(pos[1], pos[0]))

def beginCmd(unused, unused2):
    global gameBoard
    global boardSize

    pos = ai.chooseNextMove(gameBoard)
    gameBoard[pos[0]][pos[1]] = 1
    misc.printToProgram("{},{}".format(pos[1], pos[0]))

def boardCmd(unused, unused2):
    global gameBoard
    global boardSize

    line = sys.stdin.readline()
    commandTab = line.strip().split(" ")
    while commandTab[0] != "DONE":
        pos = line.strip().split(",")
        gameBoard[pos[1]][pos[0]] = pos[2]
        line = sys.stdin.readline()
        commandTab = line.strip().split(" ")

    posX, posY = misc.choosePosition(gameBoard)
    gameBoard[posY][posX] = 1
    misc.printToProgram("{},{}".format(posX, posY))

def infoCmd(key, value):
    pass

def endCmd(unused, unused2):
    sys.exit(0)

def aboutCmd(unused, unused2):
    misc.printToProgram(ABOUT)

def main():
    while True:
        line = sys.stdin.readline()
        commandTab = line.strip().split(" ")
        if commandTab[0] in COMMANDS_STR:
            param1 = commandTab[1] if len(commandTab) > 1 else 0
            param2 = commandTab[2] if len(commandTab) > 2 else 0
            globals()[FUNCTIONS_STR[COMMANDS_STR.index(commandTab[0])]](param1, param2)
        else:
            misc.printToProgram("ERROR message - unknown command \"{}\"".format(commandTab[0]))

if __name__ == "__main__":
	main()