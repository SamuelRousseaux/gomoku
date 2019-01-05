import random
import sys

def isFree(posX, posY, gameBoard):
    if gameBoard[posY][posX] == 0:
        return True
    return False

def printToProgram(thing):
    print(thing)
    sys.stdout.flush()
