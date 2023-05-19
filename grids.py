import numpy as np
import sys

""" --------------------------------------- FUNÇÕES DAS GRIDS --------------------------------------- """

# "defines"
UNKOWN = -1
WATER = 0
LEFT = 1
RIGHT = 2
TOP = 3
MIDDLE = 4
BOTTOM = 5
CENTER = 6

def create_grids_ship1(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem circle em todas posições onde pode estar na grid
    # existem no total no maximo 100 cominações diferentes de meter esse ship
    for _ in range(100):
        # cria a grid com o barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == CENTER):

            grid = [[0] * 10 for _ in range(10)]
            grid[rowIndex][columnIndex] = 1
            grids.append(grid)

        # proximo ponto
        columnIndex += 1
        if columnIndex == 10:
            columnIndex = 0
            rowIndex += 1
            # Não existe mais nenhum ponto
            if rowIndex == 10:
                break

    return grids

def create_grids_ship2_horizontal(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 90 cominações diferentes de meter esse ship na horizontal
    for _ in range(90):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == LEFT):
            
            if (board[rowIndex][columnIndex + 1] == UNKOWN or
                board[rowIndex][columnIndex + 1] == RIGHT):
                
                grid = [[0] * 10 for _ in range(10)]
                grid[rowIndex][columnIndex] = 1
                grid[rowIndex][columnIndex + 1] = 1
                grids.append(grid)
            else:
                columnIndex += 1

        # proximo ponto
        columnIndex += 1
        if columnIndex >= 9:
            columnIndex = 0
            rowIndex += 1
            # Não existe mais nenhum ponto
            if rowIndex == 10:
                break

    return grids

def create_grids_ship2_vertical(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 90 cominações diferentes de meter esse ship na vertical
    for _ in range(90):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == TOP):
            
            if (board[rowIndex + 1][columnIndex] == UNKOWN or
                board[rowIndex + 1][columnIndex] == BOTTOM):
                
                grid = [[0] * 10 for _ in range(10)]
                grid[rowIndex][columnIndex] = 1
                grid[rowIndex + 1][columnIndex] = 1
                grids.append(grid)
            else:
                rowIndex += 1

        # proximo ponto
        rowIndex += 1
        if rowIndex >= 9:
            rowIndex = 0
            columnIndex += 1
            # Não existe mais nenhum ponto
            if columnIndex == 10:
                break

    return grids

def create_grids_ship3_horizontal(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 80 cominações diferentes de meter esse ship na horizontal
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == LEFT):
            
            if (board[rowIndex][columnIndex + 1] == UNKOWN or
                board[rowIndex][columnIndex + 1] == MIDDLE):
                
                if (board[rowIndex][columnIndex + 2] == UNKOWN or
                board[rowIndex][columnIndex + 2] == RIGHT):
                    
                    grid = [[0] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = 1
                    grid[rowIndex][columnIndex + 1] = 1
                    grid[rowIndex][columnIndex + 2] = 1
                    grids.append(grid)
                else:
                    columnIndex += 2
            else:
                columnIndex += 1

        # proximo ponto
        columnIndex += 1
        if columnIndex >= 8:
            columnIndex = 0
            rowIndex += 1
            # Não existe mais nenhum ponto
            if rowIndex == 10:
                break

    return grids

def create_grids_ship3_vertical(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 cominações diferentes de meter esse ship na vertical
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == TOP):
            
            if (board[rowIndex + 1][columnIndex] == UNKOWN or
                board[rowIndex + 1][columnIndex] == MIDDLE):

                if (board[rowIndex + 2][columnIndex] == UNKOWN or
                    board[rowIndex + 2][columnIndex] == BOTTOM):
                    
                    grid = [[0] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = 1
                    grid[rowIndex + 1][columnIndex] = 1
                    grid[rowIndex + 2][columnIndex] = 1
                    grids.append(grid)
                else:
                    rowIndex += 2
            else:
                rowIndex += 1

        # proximo ponto
        rowIndex += 1
        if rowIndex >= 8:
            rowIndex = 0
            columnIndex += 1
            # Não existe mais nenhum ponto
            if columnIndex == 10:
                break

    return grids

def create_grids_ship4_horizontal(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT MIDDLE MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 70 cominações diferentes de meter esse ship na horizontal
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == LEFT):
            
            if (board[rowIndex][columnIndex + 1] == UNKOWN or
                board[rowIndex][columnIndex + 1] == MIDDLE):

                if (board[rowIndex][columnIndex + 2] == UNKOWN or
                    board[rowIndex][columnIndex + 2] == MIDDLE):
                    
                    if (board[rowIndex][columnIndex + 3] == UNKOWN or
                    board[rowIndex][columnIndex + 3] == RIGHT):
                        
                        grid = [[0] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = 1
                        grid[rowIndex][columnIndex + 1] = 1
                        grid[rowIndex][columnIndex + 2] = 1
                        grid[rowIndex][columnIndex + 3] = 1
                        grids.append(grid)
                    else:
                        columnIndex += 3
                else:
                    columnIndex += 2
            else:
                columnIndex += 1

        # proximo ponto
        columnIndex += 1
        if columnIndex >= 7:
            columnIndex = 0
            rowIndex += 1
            # Não existe mais nenhum ponto
            if rowIndex == 10:
                break

    return grids

def create_grids_ship4_vertical(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 cominações diferentes de meter esse ship na vertical
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKOWN or
            board[rowIndex][columnIndex] == TOP):
            
            if (board[rowIndex + 1][columnIndex] == UNKOWN or
                board[rowIndex + 1][columnIndex] == MIDDLE):
                
                if (board[rowIndex + 2][columnIndex] == UNKOWN or
                    board[rowIndex + 2][columnIndex] == MIDDLE):
                    
                    if (board[rowIndex + 3][columnIndex] == UNKOWN or
                        board[rowIndex + 3][columnIndex] == BOTTOM):
                        
                        grid = [[0] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = 1
                        grid[rowIndex + 1][columnIndex] = 1
                        grid[rowIndex + 2][columnIndex] = 1
                        grid[rowIndex + 3][columnIndex] = 1
                        grids.append(grid)
                    else:
                        rowIndex += 3
                else:
                    rowIndex += 2
            else:
                rowIndex += 1

        # proximo ponto
        rowIndex += 1
        if rowIndex >= 7:
            rowIndex = 0
            columnIndex += 1
            # Não existe mais nenhum ponto
            if columnIndex == 10:
                break

    return grids

def create_grids(board):
    return (create_grids_ship1(board) + 
            create_grids_ship2_horizontal(board) + create_grids_ship2_vertical(board) +
            create_grids_ship3_horizontal(board) + create_grids_ship3_vertical(board) +
            create_grids_ship4_horizontal(board) + create_grids_ship4_vertical(board))

def print_all_grids(grids):
    gridNum = 0
    for grid in grids:
        print_grid(grid)
        print()

def print_grid(grid):
    for i in range(10):
        for j in range(10):
            print(grid[i][j], end="")
        print()

board1 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

""" UNKOWN = -1, WATER = 0, LEFT = 1, RIGHT = 2, TOP = 3, MIDDLE = 4, BOTTOM = 5, CENTER = 6 """
board2 = [[-1,  0,  3,  0, -1, -1, -1, -1,  0, -1],
          [-1,  0, -1,  0, -1, -1, -1, -1,  0, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1,  0, -1],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
          [ 1, -1, -1, -1,  0, -1,  0, -1,  0, -1],
          [ 0,  0, -1, -1, -1,  4, -1, -1,  0, -1],
          [-1, -1, -1, -1,  0, -1,  0, -1,  0, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1,  0, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1,  0, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1,  0,  0]]

allGrids = create_grids(board1)
#print_all_grids(allGrids)


""" ---------------------------- AS TUAS FUNÇÕES QUE MANDASTE NO DISCORD ---------------------------- """

allGrids = create_grids()
no_ships = np.array([[-1] * 10 for _ in range(10)])
hints_pos = []
hints_matrix = np.array([[-1] * 10 for _ in range(10)])


def actions():
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        actions = []

        for i in range(len(all_grids)):
            if included[i] == 0:
                actions.append(("include", all_grids[i], i))
            elif included[i] == 1:
                actions.append(("exclude", all_grids[i], i))
        
        return actions

def result(solution_grid, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        actions(state)."""
        if action[0] == "include":
            update_solution_grid(solution_grid, action[1])
            included[action[2]] = 1
        else:
            update_solution_grid(solution_grid, action[1], include=False)
            included[action[2]] = 0

        return solution_grid

def get_combined_grid(grid1, grid):
        """Combines the grids if include = True and removes "grid" from the
        combination if include = False"""
        new_grid = [[-1 for _ in range(10)] for _ in range(10)]
        
        for i in range(10):
            for j in range(10):
                if (grid1[i][j] == 1 and grid[i][j] == 1):
                    new_grid[i][j] = 1
                elif grid1[i][j] == -1 and grid[i][j] == 1 or \
                        grid1[i][j] == 1 and grid[i][j] == -1:
                    new_grid[i][j] = 1
        
        return new_grid

def get_value(grid, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        if 0 <= row <= 9 and 0 <= col <= 9:
            return grid[row][col]
        else:
            return "None"

def adjacent_vertical_values(grid, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        return (get_value(grid, row - 1, col), get_value(grid, row + 1, col))

def adjacent_horizontal_values(grid, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        return (get_value(grid, row, col - 1), get_value(grid, row, col + 1))
    
def can_place_ship(grid, row: int, col: int):
        adj_horizontal = adjacent_horizontal_values(grid, row, col)
        adj_vertical = adjacent_vertical_values(grid, row, col)
        diagonals_left = adjacent_vertical_values(grid, row, col - 1) 
        diagonals_right = adjacent_vertical_values(grid, row, col + 1)

        for n in range(2): # They are all tuples with 2 values each
            if adj_horizontal[n] == 1 or adj_vertical[n] == 1 or \
                diagonals_left[n] == 1 or diagonals_right[n] == 1:
                return False
        return True

def interpret_hints(nhints: int):
    """Interprets the given hints, composing the 'no_ships' and 'hints_pos'
    lists that contain all positions that cannot have a ship and all positions
    that need to have a ship in the final grid, respectively"""
    for _ in range(nhints):
        hints_aux = sys.stdin.readline().strip("\n\r")
        hints_aux = hints_aux.split("\t")

        aux = tuple(map(int, hints_aux[1:3]))

        match hints_aux[3]:
            case 'W':
                hints_matrix[aux[0]][aux[1]] = WATER

                no_ships[aux[0]][aux[1]] = 1
            case 'C':
                hints_matrix[aux[0]][aux[1]] = CENTER
                hints_pos.append(tuple(map(int, aux)))

                if (aux[0]-1) != -1:
                    if (aux[1]-1) != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    no_ships[aux[0]-1][aux[1]] = 1
                    if (aux[1]+1) != 10:
                        no_ships[aux[0]-1][aux[1]+1] = 1

                if (aux[1]-1) != -1:
                    no_ships[aux[0]][aux[1]-1] = 1
                if (aux[1]+1) != 10:
                    no_ships[aux[0]][aux[1]+1] = 1

                if (aux[0]+1) != 10:
                    if (aux[1]-1) != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    no_ships[aux[0]+1][aux[1]] = 1
                    if (aux[1]+1) != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1
            case 'T':
                hints_matrix[aux[0]][aux[1]] = TOP
                hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    no_ships[aux[0]-1][aux[1]] = 1
                    if aux[1]+1 != 10: 
                        no_ships[aux[0]-1][aux[1]+1] = 1

                if aux[1]-1 != -1:
                    no_ships[aux[0]][aux[1]-1] = 1
                if aux[1]+1 != 10:
                    no_ships[aux[0]][aux[1]+1] = 1

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1
                if aux[0]+2 != 10:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+2][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+2][aux[1]+1] = 1
            case 'M':
                hints_matrix[aux[0]][aux[1]] = MIDDLE
                hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]-1][aux[1]+1] = 1

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1
            case 'B':
                hints_matrix[aux[0]][aux[1]] = BOTTOM
                hints_pos.append(tuple(map(int, aux)))

                if aux[0]-2 != -1:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-2][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]-2][aux[1]+1] = 1

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]-1][aux[1]+1] = 1

                if aux[1]-1 != -1:
                    no_ships[aux[0]][aux[1]-1] = 1
                if aux[1]+1 != 10:
                    no_ships[aux[0]][aux[1]+1] = 1

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    no_ships[aux[0]+1][aux[1]] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1
            case 'L':
                hints_matrix[aux[0]][aux[1]] = LEFT
                hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    no_ships[aux[0]-1][aux[1]] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]-1][aux[1]+1] = 1
                    if aux[1]+2 != 10:
                        no_ships[aux[0]-1][aux[1]+2] = 1

                if aux[1]-1 != -1:
                    no_ships[aux[0]][aux[1]-1] = 1

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    no_ships[aux[0]+1][aux[1]] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1
                    if aux[1]+2 != 10:
                        no_ships[aux[0]+1][aux[1]+2] = 1
            case 'R':
                hints_matrix[aux[0]][aux[1]] = RIGHT
                hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-2 != -1:
                        no_ships[aux[0]-1][aux[1]-2] = 1
                    if aux[1]-1 != -1:
                        no_ships[aux[0]-1][aux[1]-1] = 1
                    no_ships[aux[0]-1][aux[1]] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]-1][aux[1]+1] = 1

                if aux[1]+1 != 10:
                    no_ships[aux[0]][aux[1]+1] = 1

                if aux[0]+1 != 10:
                    if aux[1]-2 != -1:
                        no_ships[aux[0]+1][aux[1]-2] = 1
                    if aux[1]-1 != -1:
                        no_ships[aux[0]+1][aux[1]-1] = 1
                    no_ships[aux[0]+1][aux[1]] = 1
                    if aux[1]+1 != 10:
                        no_ships[aux[0]+1][aux[1]+1] = 1

solution_grid = np.zeros((10,10), dtype=np.int8)

from sys import stdin
rows_nships = stdin.readline().strip("\n")
rows_nships = rows_nships.split("\t")
rows_nships = rows_nships[1:]
rows_nships = (tuple(map(int, rows_nships)))

cols_nships = stdin.readline().strip("\n")
cols_nships = cols_nships.split("\t")
cols_nships = cols_nships[1:]
cols_nships = (tuple(map(int, cols_nships)))

nhints = int(input())

# Builds the 'no_ship' and 'hints_pos' lists
interpret_hints(nhints)

print("position of the hints (ships): ", hints_pos)
print("hints matrix:\n", hints_matrix)
print("positions with no ships:\n", no_ships)

print(np.array(allGrids[0]))
print(adjacent_horizontal_values(allGrids[0], 0, 0))
print(can_place_ship(allGrids[0], 0, 0))

print(np.array(allGrids[115]))
print(np.array(get_combined_grid(allGrids[0], allGrids[115])))