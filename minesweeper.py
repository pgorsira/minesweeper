__author__ = "Pieter Gorsira"

import random

side = 9
mines = 10
picks = 0
lost = False
use_solver = True

sol_board = [[0 for x in range(side)] for y in range(side)]  # solution (full board)
usr_board = [['_' for x in range(side)] for y in range(side)]  # user's current board configuration


def solver():



def display(board):
    s = [[str(e) for e in row] for row in board]
    lens = [len(max(col, key=len)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)
    print '\n'


def reveal_zeros(x, y):
    global usr_board
    if sol_board[x][y] == 0:
        usr_board[x][y] = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                try:
                    if x+dx >= 0 and y+dy >= 0 and usr_board[x+dx][y+dy] != 0:
                        reveal_zeros(x+dx, y+dy)
                except IndexError, e:
                    continue


def check_win():
    won = True
    for i in range(len(sol_board)):
        for j in range(len(sol_board[i])):
            if sol_board[i][j] != usr_board[i][j] and sol_board[i][j] != '*':
                won = False
                break
        if not won:
            break
    return won


def pick(x, y):
    global usr_board
    global picks
    global lost
    picks += 1
    if sol_board[x][y] == '*':  # picked a mine, show all mines and 'X' offending mine
        for i in range(len(sol_board)):
            for j in range(len(sol_board[i])):
                if sol_board[i][j] == '*':
                    usr_board[i][j] = '*'
        usr_board[x][y] = 'X'
        lost = True
    elif sol_board[x][y] == 0:  # picked a 0, open all adjacent 0s (and their adjacent 0s)
        reveal_zeros(x, y)
    else:  # picked a nonzero number, just show number
        usr_board[x][y] = sol_board[x][y]


while mines > 0:  # prepare board
    x = random.randrange(0, side)
    y = random.randrange(0, side)

    sol_board[x][y] = '*'

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            try:
                if sol_board[x+dx][y+dy] != '*' and x+dx >= 0 and y+dy >= 0:
                    sol_board[x+dx][y+dy] += 1
            except IndexError, e:
                continue

    mines -= 1

print "Welcome to minesweeper\n"
display(usr_board)
# display(sol_board)

while not (check_win() or lost):
    if use_solver:
        coord = solver()
        x = coord[0]
        y = coord[1]
    else:
        x = int(raw_input("x: "))
        y = int(raw_input("y: "))

    if x >= side or y >= side or x < 0 or y < 0:
        print "Not a valid coordinate\n"
        continue

    pick(x, y)
    display(usr_board)

if lost:
    print "You have lost"
else:
    print "You have won in " + str(picks) + " turns"





