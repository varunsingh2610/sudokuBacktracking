#!/usr/bin/python3
board = [
        [0,0,5,4,9,0,0,0,8],
        [2,0,0,8,5,1,0,0,0],
        [0,1,0,7,0,0,5,2,0],
        [0,0,0,0,0,0,0,5,3],
        [0,0,2,3,0,8,4,0,0],
        [1,3,0,0,0,0,0,0,0],
        [0,7,4,0,0,5,0,6,0],
        [0,0,0,1,8,7,0,0,5],
        [5,0,0,0,3,4,7,0,0]
]

def solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def check(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

printBoard(board)
solve(board)
print("-------Solution--------")
printBoard(board)
