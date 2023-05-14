from sys import stdin
import numpy as np

rows_nships = stdin.readline().strip("\n")
rows_nships = rows_nships.split("\t")
rows_nships = rows_nships[1:]
rows_nships = (tuple(map(int, rows_nships)))
print('number of ships required per row: ', rows_nships)
cols_nships = stdin.readline().strip("\n")
cols_nships = cols_nships.split("\t")
cols_nships = cols_nships[1:]
cols_nships = (tuple(map(int, cols_nships)))
print('number of ships required per col: ', cols_nships)
nhints = int(input())
print('number of hints: ', nhints)

# M[i][j] is 0 if cell(i,j) contains water in the initial grid, 1 if it contains
# a piece of a ship, and 100 otherwise
M = np.array(np.array([[100] * 10 for _ in range(10)])) # Without the np.array's ?

no_ship = []
hints_pos = []
for _ in range(nhints):
    hints_aux = stdin.readline().strip("\n\r")
    hints_aux = hints_aux.split("\t")
    print(hints_aux)

    aux = tuple(map(int, hints_aux[1:3]))
    print(aux)
    match hints_aux[3]:
        case 'W':
            M[aux[0]][aux[1]] = 0

            no_ship.append(aux)
        case 'C':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1])))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0], aux[1]-1)))
            no_ship.append(tuple((aux[0], aux[1]+1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1])))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))
        case 'T':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1])))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0], aux[1]-1)))
            no_ship.append(tuple((aux[0], aux[1]+1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))
        case 'M':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))
        case 'B':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0], aux[1]-1)))
            no_ship.append(tuple((aux[0], aux[1]+1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1])))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))
        case 'L':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1])))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0], aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1])))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))
        case 'R':
            M[aux[0]][aux[1]] = 1
            hints_pos.append(tuple(map(int, aux)))

            no_ship.append(tuple((aux[0]-1, aux[1]-1)))
            no_ship.append(tuple((aux[0]-1, aux[1])))
            no_ship.append(tuple((aux[0]-1, aux[1]+1)))
            no_ship.append(tuple((aux[0], aux[1]+1)))
            no_ship.append(tuple((aux[0]+1, aux[1]-1)))
            no_ship.append(tuple((aux[0]+1, aux[1])))
            no_ship.append(tuple((aux[0]+1, aux[1]+1)))

print('position of the ships on the initial grid (hints): ', hints_pos)
print('positions that CANNOT have ships: ', no_ship)

print(M)