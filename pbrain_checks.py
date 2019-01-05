import pbrain_misc as misc

def checkIfFirstMove(board):
    for line in board:
        if 1 in line:
            return None

    lenBoard = len(board)
    mid = int(lenBoard / 2) - 1

    if misc.isFree(mid, mid, board) == True:
        return [mid, mid]
    return [mid, mid + 1]

def checkHorizontal(pattern, board, j, i):
    for x in range(i, i + len(pattern)):
        if x > len(board) - 1:
            ret = None
            break
        if board[j][x] != int(pattern[x - i]):
            ret = None
            break
        if pattern[x - i] == "0":
            ret = [j, x]
    if ret != None:
        return ret

    for x in range(i, i - len(pattern), -1):
        if x < 0:
            ret = None
            break
        if board[j][x] != int(pattern[-(x - i)]):
            ret = None
            break
        if pattern[-(x - i)] == "0":
            ret = [j, x]
    return ret

def checkVertical(pattern, board, j, i):
    for y in range(j, j + len(pattern)):
        if y > len(board) - 1:
            ret = None
            break
        if board[y][i] != int(pattern[y - j]):
            ret = None
            break
        if pattern[y - j] == "0":
            ret = [y, i]
    if ret != None:
        return ret

    for y in range(j, j - len(pattern), -1):
        if y < 0:
            ret = None
            break
        if board[y][i] != int(pattern[-(y - j)]):
            ret = None
            break
        if pattern[-(y - j)] == "0":
            ret = [y, i]
    return ret

def checkDiagonalUp(pattern, board, j, i):
    for x in range(0, len(pattern)):
        if j - x < 0 or x + i > len(board) - 1:
            ret = None
            break
        if board[j - x][i + x] != int(pattern[x]):
            ret = None
            break
        if pattern[x] == "0":
            ret = [j - x, i + x]
    if ret != None:
        return ret

    for x in range(0, len(pattern)):
        if j + x > len(board) - 1 or i - x < 0:
            ret = None
            break
        if board[j + x][i - x] != int(pattern[x]):
            ret = None
            break
        if pattern[x] == "0":
            ret = [j + x, i - x]
    return ret

def checkDiagonalDown(pattern, board, j, i):
    for x in range(0, len(pattern)):
        if j + x > len(board) - 1 or i + x > len(board) - 1:
            ret = None
            break
        if board[j + x][i + x] != int(pattern[x]):
            ret = None
            break
        if pattern[x] == "0":
            ret = [j + x, i + x]
    if ret != None:
        return ret

    for x in range(0, len(pattern)):
        if j - x < 0 or i - x < 0:
            ret = None
            break
        if board[j - x][i - x] != int(pattern[x]):
            ret = None
            break
        if pattern[x] == "0":
            ret = [j - x, i - x]
    return ret