import pbrain_checks as check
import pbrain_misc as misc
import random

patterns = [ "11011", "11110", "11101", "22022", "22220", "22202", "2202", "2220", "1101", "1110", "110", "101", "10" ]

def chooseRandomMove(gameBoard, boardSize):
    posX = random.randint(0, boardSize - 1)
    posY = random.randint(0, boardSize - 1)
    while (misc.isFree(posX, posY, gameBoard) == False):
        posX = random.randint(0, boardSize - 1)
        posY = random.randint(0, boardSize - 1)
    return [posY, posX]

def checkPattern(pattern, board, j, i):
    ret = check.checkHorizontal(pattern, board, j, i)
    if ret != None:
        return ret
    ret = check.checkVertical(pattern, board, j, i)
    if ret != None:
        return ret
    ret = check.checkDiagonalUp(pattern, board, j, i)
    if ret != None:
        return ret
    ret = check.checkDiagonalDown(pattern, board, j, i)
    if ret != None:
        return ret
    return None


def validMove(move, board):
    if move[0] < 0 or move[0] >= len(board):
        return False
    elif move[1] < 0 or move[1] >= len(board):
        return False
    return True


def chooseNextMove(board):
    ret = check.checkIfFirstMove(board)
    if ret != None:
        return ret
    for pattern in patterns:
        for j in range(len(board)):
            for i in range(len(board)):
                if board[j][i] == 1 or board[j][i] == 2:
                    ret = checkPattern(pattern, board, j, i)
                    if ret != None and validMove(ret, board) == True:
                        return ret
    return chooseRandomMove(board, len(board))