# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 115:
# 103811 Tiago Deane
# 104145 Artur Krystopchuk

# Defines
UNKNOWN = -1
WATER = 0
LEFT = 1
RIGHT = 2
TOP = 3
BOTTOM = 4
MIDDLE = 5
CENTER = 6

import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)

def create_hint_ships(hints, starting_board):
    """Creates all the ships that could be used to solve the given hints, and
    returns the 'no_ships' set that will be given as an argument to the ship
    creation functions to make sure they don't create any repeated or
    unnecessary ship grids"""

    # Stores the position around the hints
    # The positions are stored as numbers in the format "row*10 + col"
    no_ships = set()

    for pos in Board.hints_pos:
        row = pos[0]
        col = pos[1]

        if hints[row][col] == WATER:
            continue # Water is always already placed in the starting grid
        
        elif hints[row][col] == LEFT:
            # Creates every ship grid that could solve a "LEFT" hint
            if col <= 6:
                if starting_board.can_place_ship2_h(row, col):
                    Board.grids_ship2_hor.append(((row, col), 2, 'hor'))
                if starting_board.can_place_ship3_h(row, col):
                    Board.grids_ship3_hor.append(((row, col), 3, 'hor'))
                if starting_board.can_place_ship4_h(row, col):
                    Board.grids_ship4_hor.append(((row, col), 4, 'hor'))
            elif col == 7:
                if starting_board.can_place_ship2_h(row, col):
                    Board.grids_ship2_hor.append(((row, col), 2, 'hor'))
                if starting_board.can_place_ship3_h(row, col):
                    Board.grids_ship3_hor.append(((row, col), 3, 'hor'))
            elif col == 8:
                Board.grids_ship2_hor.append(((row, col), 2, 'hor'))

        elif hints[row][col] == RIGHT:
            # Creates every ship grid that could solve a "RIGHT" hint
            if col >= 3:
                if starting_board.can_place_ship2_h(row, col-1):
                    Board.grids_ship2_hor.append(((row, col-1), 2, 'hor'))
                if starting_board.can_place_ship3_h(row, col-2):
                    Board.grids_ship3_hor.append(((row, col-2), 3, 'hor'))
                if starting_board.can_place_ship4_h(row, col-3):
                    Board.grids_ship4_hor.append(((row, col-3), 4, 'hor'))
            elif col == 2:
                if starting_board.can_place_ship2_h(row, col-1):
                    Board.grids_ship2_hor.append(((row, col-1), 2, 'hor'))
                if starting_board.can_place_ship3_h(row, col-2):
                    Board.grids_ship3_hor.append(((row, col-2), 3, 'hor'))
            elif col == 1:
                Board.grids_ship2_hor.append(((row, col-1), 2, 'hor'))

        elif hints[row][col] == TOP:
            # Creates every ship grid that could solve a "TOP" hint
            if row <= 6:
                if starting_board.can_place_ship2_v(row, col):
                    Board.grids_ship2_ver.append(((row, col), 2, 'ver'))
                if starting_board.can_place_ship3_v(row, col):
                    Board.grids_ship3_ver.append(((row, col), 3, 'ver'))
                if starting_board.can_place_ship4_v(row, col):
                    Board.grids_ship4_ver.append(((row, col), 4, 'ver'))
            elif row == 7:
                if starting_board.can_place_ship2_v(row, col):
                    Board.grids_ship2_ver.append(((row, col), 2, 'ver'))
                if starting_board.can_place_ship3_v(row, col):
                    Board.grids_ship3_ver.append(((row, col), 3, 'ver'))
            elif row == 8:
                Board.grids_ship2_ver.append(((row, col), 2, 'ver'))
        
        elif hints[row][col] == BOTTOM:
            # Creates every ship grid that could solve a "BOTTOM" hint
            if row >= 3:
                if starting_board.can_place_ship2_v(row-1, col):
                    Board.grids_ship2_ver.append(((row-1, col), 2, 'ver'))
                if starting_board.can_place_ship3_v(row-2, col):
                    Board.grids_ship3_ver.append(((row-2, col), 3, 'ver'))
                if starting_board.can_place_ship4_v(row-3, col):
                    Board.grids_ship4_ver.append(((row-3, col), 4, 'ver'))
            elif row == 2:
                if starting_board.can_place_ship2_v(row-1, col):
                    Board.grids_ship2_ver.append(((row-1, col), 2, 'ver'))
                if starting_board.can_place_ship2_v(row-2, col):
                    Board.grids_ship3_ver.append(((row-2, col), 3, 'ver'))
            elif row == 1:
                Board.grids_ship2_ver.append(((row-1, col), 2, 'ver'))
        
        elif hints[row][col] == MIDDLE:
            # Creates every ship grid that could solve a "MIDDLE" hint
            if 2 <= col <= 7:
                if starting_board.can_place_ship3_h(row, col-1):
                    Board.grids_ship3_hor.append(((row, col-1), 3, 'hor'))
                if starting_board.can_place_ship4_h(row, col-1):
                    Board.grids_ship4_hor.append(((row, col-1), 4, 'hor'))
                if starting_board.can_place_ship4_h(row, col-2):
                    Board.grids_ship4_hor.append(((row, col-2), 4, 'hor'))
            elif col == 1:
                if starting_board.can_place_ship3_h(row, col-1):
                    Board.grids_ship3_hor.append(((row, col-1), 3, 'hor'))
                if starting_board.can_place_ship4_h(row, col-1):
                    Board.grids_ship4_hor.append(((row, col-1), 4, 'hor'))
            elif col == 8:
                if starting_board.can_place_ship3_h(row, col-1):
                    Board.grids_ship3_hor.append(((row, col-1), 3, 'hor'))
                if starting_board.can_place_ship4_h(row, col-2):
                    Board.grids_ship4_hor.append(((row, col-2), 4, 'hor'))

            if 2 <= row <= 7:
                if starting_board.can_place_ship3_v(row-1, col):
                    Board.grids_ship3_ver.append(((row-1, col), 3, 'ver'))
                if starting_board.can_place_ship4_v(row-1, col):
                    Board.grids_ship4_ver.append(((row-1, col), 4, 'ver'))
                if starting_board.can_place_ship4_v(row-2, col):
                    Board.grids_ship4_ver.append(((row-2, col), 4, 'ver'))
            elif row == 1:
                if starting_board.can_place_ship3_v(row-1, col):
                    Board.grids_ship3_ver.append(((row-1, col), 3, 'ver'))
                if starting_board.can_place_ship4_v(row-1, col):
                    Board.grids_ship4_ver.append(((row-1, col), 4, 'ver'))
            elif row == 8:
                if starting_board.can_place_ship3_v(row-1, col):
                    Board.grids_ship3_ver.append(((row-1, col), 3, 'ver'))
                if starting_board.can_place_ship4_v(row-2, col):
                    Board.grids_ship4_ver.append(((row-2, col), 4, 'ver'))


        # Guarantees no more ship grids are created around the hint's position
        if row-1 >= 0:
            if col-1 >= 0:
                no_ships.add((row-1)*10 + (col-1))
            no_ships.add((row-1)*10 + col)
            if col+1 <= 9:
                no_ships.add((row-1)*10 + (col+1))
        if col-1 >= 0:
            no_ships.add(row*10 + (col-1))
        no_ships.add(row*10 + col)
        if col+1 <= 9:
            no_ships.add(row*10 + (col+1))
        if row+1 <= 9:
            if col-1 >= 0:
                no_ships.add((row+1)*10 + (col-1))
            no_ships.add((row+1)*10 + col)
            if col+1 <= 9:
                no_ships.add((row+1)*10 + (col+1))

    return no_ships


def create_grids_ship1(hints, starting_board, no_ships):
    """Creates every grid with size 1 ships, except the ones that are given in
    the hints. Iterates from left to right."""
    row = 0
    col = 0

    # Existem no total no maximo 100 combinações diferentes de meter esse ship
    for _ in range(100):

        # Checks if the ship is around any hint's position
        if (row*10 + col) in no_ships:
            col += 1
            if col >= 10:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Checks if the row has enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

        # Checks if the column has enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col == 10:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        
        # Cria a grid com o barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == CENTER) and\
            starting_board.grid[row][col] == UNKNOWN:

            grid = ((row, col), 1, "hor")

            Board.grids_ship1.append(grid)

        # Proximo ponto
        col += 1
        if col == 10:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break


def create_grids_ship2_horizontal(hints, starting_board, no_ships):
    """Creates every grid with size 2 horizontal ships, except the ones that
    could be used to solve the given hints. Iterates from left to right."""
    row = 0
    col = 0

    # Existem no total no maximo 90 combinações diferentes de meter esse ship na horizontal
    for _ in range(90):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            col += 1
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+1)) in no_ships:
            col += 2
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]\
                or Board.rows_nships[row] < 2\
                or starting_board.ships_placed_rows[row] + 2 > Board.rows_nships[row]:
            col += 1
            if col >= 9:
                col = 0
                row += 1
                if row == 10:
                    break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif starting_board.ships_placed_cols[col+1] == Board.cols_nships[col+1]:
            col += 2
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == LEFT) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row][col+1] == UNKNOWN:
            
            if (hints[row][col + 1] == UNKNOWN or
                hints[row][col + 1] == RIGHT):
                
                grid = ((row, col), 2, "hor")

                Board.grids_ship2_hor.append(grid)

        # proximo ponto
        col += 1
        if col >= 9:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break


def create_grids_ship2_vertical(hints, starting_board, no_ships):
    """Creates every grid with size 2 vertical ships, except the ones that could
    be used to solve the given hints. Iterates from top to bottom."""
    row = 0
    col = 0

    # Existem no total no maximo 90 combinações diferentes de meter esse ship na vertical
    for _ in range(90):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            row += 1
            if row >= 9:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+1)*10 + col) in no_ships:
            row += 2
            if row >= 9:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]\
                or Board.cols_nships[col] < 2\
                or starting_board.ships_placed_cols[col] + 2 > Board.cols_nships[col]:
            col += 1
            row = 0
            # Não existe mais nenhum ponto
            if col == 10:
                break
            continue
        
        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]:
            row += 1
            if row >= 9:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+1] == Board.rows_nships[row+1]:
            row += 2
            if row >= 9:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue

        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == TOP) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row+1][col] == UNKNOWN:
            
            if (hints[row + 1][col] == UNKNOWN or
                hints[row + 1][col] == BOTTOM):
                
                grid = ((row, col), 2, "ver")

                Board.grids_ship2_ver.append(grid)

        # proximo ponto
        row += 1
        if row >= 9:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
                break


def create_grids_ship3_horizontal(hints, starting_board, no_ships):
    """Creates every grid with size 3 horizontal ships, except the ones that
    could be used to solve the given hints. Iterates from left to right."""
    row = 0
    col = 0

    # Existem no total no maximo 80 combinações diferentes de meter esse ship na horizontal
    for _ in range(80):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            col += 1
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+1)) in no_ships:
            col += 2
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+2)) in no_ships:
            col += 3
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]\
                or Board.rows_nships[row] < 3\
                or starting_board.ships_placed_rows[row] + 3 > Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+1] == Board.cols_nships[col+1]:
            col += 2
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+2] == Board.cols_nships[col+2]:
            col += 3
            if col >= 8:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == LEFT) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row][col+1] == UNKNOWN and\
            starting_board.grid[row][col+2] == UNKNOWN:
            
            if (hints[row][col + 1] == UNKNOWN or
                hints[row][col + 1] == MIDDLE):
                
                if (hints[row][col + 2] == UNKNOWN or
                hints[row][col + 2] == RIGHT):
                    
                    grid = ((row, col), 3, "hor")

                    Board.grids_ship3_hor.append(grid)

        # proximo ponto
        col += 1
        if col >= 8:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break


def create_grids_ship3_vertical(hints, starting_board, no_ships):
    """Creates every grid with size 3 vertical ships, except the ones that could
    be used to solve the given hints. Iterates from top to bottom."""
    row = 0
    col = 0

    # Existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(80):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            row += 1
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+1)*10 + col) in no_ships:
            row += 2
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+2)*10 + col) in no_ships:
            row += 3
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]\
                or Board.cols_nships[col] < 3\
                or starting_board.ships_placed_cols[col]+3 > Board.cols_nships[col]:
            col += 1
            row = 0
            if col == 10:
                break
            continue

        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]:
            row += 1
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+1] == Board.rows_nships[row+1]:
            row += 2
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+2] == Board.rows_nships[row+2]:
            row += 3
            if row >= 8:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        
        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == TOP) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row+1][col] == UNKNOWN and\
            starting_board.grid[row+2][col] == UNKNOWN:
            
            if (hints[row + 1][col] == UNKNOWN or
                hints[row + 1][col] == MIDDLE):

                if (hints[row + 2][col] == UNKNOWN or
                    hints[row + 2][col] == BOTTOM):
                    
                    grid = ((row, col), 3, "ver")
                    
                    Board.grids_ship3_ver.append(grid)

        # proximo ponto
        row += 1
        if row >= 8:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
                break


def create_grids_ship4_horizontal(hints, starting_board, no_ships):
    """Creates every grid with size 4 horizontal ships, except the ones that
    could be used to solve the given hints. Iterates from left to right."""
    row = 0
    col = 0
    
    # existem no total no maximo 70 combinações diferentes de meter esse ship na horizontal
    for _ in range(70):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            col += 1
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+1)) in no_ships:
            col += 2
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+2)) in no_ships:
            col += 3
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        elif (row*10 + (col+3)) in no_ships:
            col += 4
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row] or Board.rows_nships[row] < 4\
                or starting_board.ships_placed_rows[row] + 4 > Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+1] == Board.cols_nships[col+1]:
            col += 2
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+2] == Board.cols_nships[col+2]:
            col += 3
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+3] == Board.cols_nships[col+3]:
            col += 4
            if col >= 7:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == LEFT) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row][col+1] == UNKNOWN and\
            starting_board.grid[row][col+2] == UNKNOWN and\
            starting_board.grid[row][col+3] == UNKNOWN:
            
            if (hints[row][col + 1] == UNKNOWN or
                hints[row][col + 1] == MIDDLE):

                if (hints[row][col + 2] == UNKNOWN or
                    hints[row][col + 2] == MIDDLE):
                    
                    if (hints[row][col + 3] == UNKNOWN or
                    hints[row][col + 3] == RIGHT):
                        
                        grid = ((row, col), 4, "hor")
                        
                        Board.grids_ship4_hor.append(grid)

        # proximo ponto
        col += 1
        if col >= 7:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break


def create_grids_ship4_vertical(hints, starting_board, no_ships):
    """Creates every grid with size 4 vertical ships, except the ones that could
    be used to solve the given hints. Iterates from top to bottom."""
    row = 0
    col = 0

    # Existem no total no maximo 70 combinações diferentes de meter esse ship na vertical
    for _ in range(70):

        # Checks if the ships are around any hint's position
        if (row*10 + col) in no_ships:
            row += 1
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+1)*10 + col) in no_ships:
            row += 2
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+2)*10 + col) in no_ships:
            row += 3
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        elif ((row+3)*10 + col) in no_ships:
            row += 4
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue

        # Checks if the columns have enough capacity for the ship to fit
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col] or Board.cols_nships[col] < 4\
                or starting_board.ships_placed_cols[col] + 4 > Board.cols_nships[col]:
            col += 1
            row = 0
            if col == 10:
                break
            continue

        # Checks if the rows have enough capacity for the ship to fit
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]:
            row += 1
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+1] == Board.rows_nships[row+1]:
            row += 2
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+2] == Board.rows_nships[row+2]:
            row += 3
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue
        if starting_board.ships_placed_rows[row+3] == Board.rows_nships[row+3]:
            row += 4
            if row >= 7:
                row = 0
                col += 1
                # Não existe mais nenhum ponto
                if col == 10:
                    break
            continue

        # Cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == TOP) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row+1][col] == UNKNOWN and\
            starting_board.grid[row+2][col] == UNKNOWN and\
            starting_board.grid[row+3][col] == UNKNOWN:
            
            if (hints[row + 1][col] == UNKNOWN or
                hints[row + 1][col] == MIDDLE):
                
                if (hints[row + 2][col] == UNKNOWN or
                    hints[row + 2][col] == MIDDLE):
                    
                    if (hints[row + 3][col] == UNKNOWN or
                        hints[row + 3][col] == BOTTOM):
                        
                        grid = ((row, col), 4, "ver")
                        
                        Board.grids_ship4_ver.append(grid)

        # proximo ponto
        row += 1
        if row >= 7:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
                break


def create_grids(hints, starting_board):
    """Receives a grid with the ships given in the hints and creates all
    possible grids that can be used to solve the puzzle."""

    # 'no_ships' stores the positions around the hints;
    # create_hint_ships creates the ships that could be used to solve the hints.
    no_ships = create_hint_ships(hints, starting_board)

    # Creates all grids, except those that could be used to solve the hints or
    # that occupy the spaces around said hints.
    create_grids_ship1(hints, starting_board, no_ships)
    create_grids_ship2_horizontal(hints, starting_board, no_ships)
    create_grids_ship2_vertical(hints, starting_board, no_ships)
    create_grids_ship3_horizontal(hints, starting_board, no_ships)
    create_grids_ship3_vertical(hints, starting_board, no_ships)
    create_grids_ship4_horizontal(hints, starting_board, no_ships)
    create_grids_ship4_vertical(hints, starting_board, no_ships)


class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id


class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    # Saves the number of ships required in each row and column from 0 to 9.
    # They are constructed during parse_instance()
    rows_nships = []
    cols_nships = []

    # Saves the positions that MUST have ships in the final solution.
    # This list is constructed during interpret_hints()
    hints_pos = []

    # Lists of ship grids
    """Note: a ship grid is a tuple with the format ((row,col), size, orientation),
    where (row,col) is the ship's first position, size is the ship's size and
    orientation is either 'hor' (horizontal) or 'ver' (vertical)"""
    grids_ship1 = []
    grids_ship2_hor = []
    grids_ship2_ver = []
    grids_ship3_hor = []
    grids_ship3_ver = []
    grids_ship4_hor = []
    grids_ship4_ver = []

    def __init__(self, grid, nships_of_size, ships_placed_rows, ships_placed_cols):
        # The Board's grid is a 10x10 grid that represents the puzzle's board
        self.grid = grid

        # ships_placed_rows[i] stores how many ships have been placed in row i
        if len(ships_placed_rows) == 0:
            self.ships_placed_rows = [0 for _ in range(10)]
        else:
            self.ships_placed_rows = ships_placed_rows
        
        # ships_placed_cols[j] stores how many ships have been placed in column j
        if len(ships_placed_cols) == 0:
            self.ships_placed_cols = [0 for _ in range(10)]
        else:
            self.ships_placed_cols = ships_placed_cols

        # Index 'i' of nships_of_size has the number of ships of size i+1
        # placed in this Board's grid
        if len(nships_of_size) == 0:
            self.nships_of_size = [0 for _ in range(4)]
        else:
            self.nships_of_size = nships_of_size

    def get_value(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição da representação do tabuleiro."""
        if 0 <= row <= 9 and 0 <= col <= 9:
            return self.grid[row][col]
        else:
            return UNKNOWN

    def adjacent_vertical_values(self, row: int, col: int) -> (int, int):
        """Devolve os valores inteiros imediatamente acima e abaixo,
        respectivamente."""
        return (self.get_value(row-1, col), self.get_value(row+1, col))

    def adjacent_horizontal_values(self, row: int, col: int) -> (int, int):
        """Devolve os valores inteiros imediatamente à esquerda e à direita,
        respectivamente."""
        return (self.get_value(row, col-1), self.get_value(row, col+1))
    
    def no_ships_around(self, row: int, col: int):
        """Returns True if a ship can be placed in the given position"""

        adj_horizontal = self.adjacent_horizontal_values(row, col)
        adj_vertical = self.adjacent_vertical_values(row, col)
        diagonals_left = self.adjacent_vertical_values(row, col - 1)
        diagonals_right = self.adjacent_vertical_values(row, col + 1)

        # Checks if none of the positions around (row, col) have ships
        for n in range(2): # They are all tuples with 2 values each
            if adj_horizontal[n] > 0 or adj_vertical[n] > 0 or \
                diagonals_left[n] > 0 or diagonals_right[n] > 0:
                return False
        
        return True

    def can_place_ship1(self, row: int, col: int):
        """Returns True if a size 1 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or\
                self.ships_placed_rows[row] == Board.rows_nships[row] or\
                self.ships_placed_cols[col] == Board.cols_nships[col]:
            return False
        
        return self.no_ships_around(row, col)
    
    def can_place_ship2_h(self, row: int, col: int):
        """Returns True if a horizontal size 2 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row, col+1) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row] or\
                self.ships_placed_cols[col] == Board.cols_nships[col] or\
                self.ships_placed_cols[col+1] == Board.cols_nships[col+1] or\
                self.ships_placed_rows[row]+2 > Board.rows_nships[row]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row, col+1)
    
    def can_place_ship2_v(self, row: int, col: int):
        """Returns True if a vertical size 2 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row+1, col) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row]\
                or self.ships_placed_rows[row+1] == Board.rows_nships[row+1]\
                or self.ships_placed_cols[col] == Board.cols_nships[col]\
                or self.ships_placed_cols[col]+2 > Board.cols_nships[col]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row+1, col)
    
    def can_place_ship3_h(self, row: int, col: int):
        """Returns True if a horizontal size 3 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row, col+1) != UNKNOWN\
                or self.get_value(row, col+2) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row]\
                or self.ships_placed_cols[col] == Board.cols_nships[col]\
                or self.ships_placed_cols[col+1] == Board.cols_nships[col+1]\
                or self.ships_placed_cols[col+2] == Board.cols_nships[col+2]\
                or self.ships_placed_rows[row]+3 > Board.rows_nships[row]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row, col+1)\
                and self.no_ships_around(row, col+2)
    
    def can_place_ship3_v(self, row: int, col: int):
        """Returns True if a vertical size 3 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row+1, col) != UNKNOWN\
                or self.get_value(row+2, col) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row]\
                or self.ships_placed_rows[row+1] == Board.rows_nships[row+1]\
                or self.ships_placed_rows[row+2] == Board.rows_nships[row+2]\
                or self.ships_placed_cols[col] == Board.cols_nships[col]\
                or self.ships_placed_cols[col]+3 > Board.cols_nships[col]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row+1, col)\
                and self.no_ships_around(row+2, col)
    
    def can_place_ship4_h(self, row: int, col: int):
        """Returns True if a horizontal size 4 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row, col+1) != UNKNOWN\
                or self.get_value(row, col+2) != UNKNOWN\
                or self.get_value(row, col+3) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row]\
                or self.ships_placed_cols[col] == Board.cols_nships[col]\
                or self.ships_placed_cols[col+1] == Board.cols_nships[col+1]\
                or self.ships_placed_cols[col+2] == Board.cols_nships[col+2]\
                or self.ships_placed_cols[col+3] == Board.cols_nships[col+3]\
                or self.ships_placed_rows[row]+4 > Board.rows_nships[row]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row, col+1)\
            and self.no_ships_around(row, col+2) and self.no_ships_around(row, col+3) 
    
    def can_place_ship4_v(self, row: int, col: int):
        """Returns True if a vertical size 4 ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN or self.get_value(row+1, col) != UNKNOWN\
                or self.get_value(row+2, col) != UNKNOWN\
                or self.get_value(row+3, col) != UNKNOWN\
                or self.ships_placed_rows[row] == Board.rows_nships[row]\
                or self.ships_placed_cols[col] == Board.cols_nships[col]\
                or self.ships_placed_rows[row+1] == Board.rows_nships[row+1]\
                or self.ships_placed_rows[row+2] == Board.rows_nships[row+2]\
                or self.ships_placed_rows[row+3] == Board.rows_nships[row+3]\
                or self.ships_placed_cols[col]+4 > Board.cols_nships[col]:
            return False
        
        return self.no_ships_around(row, col) and self.no_ships_around(row+1, col)\
            and self.no_ships_around(row+2, col) and self.no_ships_around(row+3, col)   
    
    def check_objective(self):
        """Returns True if the Board's grid is the puzzle's solution"""
        
        # Checks if all rows and columns have the required number of ships
        for n in range(10):
            if self.ships_placed_rows[n] != Board.rows_nships[n] or\
                    self.ships_placed_cols[n] != Board.cols_nships[n]:
                return False

        # Checks if all hint position have ships in them
        for pos in self.hints_pos:
            if self.grid[pos[0]][pos[1]] == UNKNOWN:
                return False
        
        # Checks if there are 4 size 1 ships, 3 size 2 ships,
        # 2 size 3 ships and 1 size 4 ship
        if self.nships_of_size[0] != 4 or self.nships_of_size[1] != 3 or\
            self.nships_of_size[2] != 2 or self.nships_of_size[3] != 1:
            return False
                
        return True

    def add_ship(self, ship_grid):
        """Returns a new 10x10 grid that is the result of placing the
        ship_grid's ship in this Board's grid"""
        new_grid = [row[:] for row in self.grid] # hard copy of this board's grid

        # Ship grids are a tuple with the format ((row, col), size, orientation)
        row = ship_grid[0][0]
        col = ship_grid[0][1]
        size = ship_grid[1]
        orientation = ship_grid[2]
        
        if size == 4:
            if orientation == "hor":
                new_grid[row][col] = LEFT
                new_grid[row][col+1] = MIDDLE
                new_grid[row][col+2] = MIDDLE
                new_grid[row][col+3] = RIGHT
            else:
                new_grid[row][col] = TOP
                new_grid[row+1][col] = MIDDLE
                new_grid[row+2][col] = MIDDLE
                new_grid[row+3][col] = BOTTOM
        elif size == 3:
            if orientation == "hor":
                new_grid[row][col] = LEFT
                new_grid[row][col+1] = MIDDLE
                new_grid[row][col+2] = RIGHT
            else:
                new_grid[row][col] = TOP
                new_grid[row+1][col] = MIDDLE
                new_grid[row+2][col] = BOTTOM
        elif size == 2:
            if orientation == "hor":
                new_grid[row][col] = LEFT
                new_grid[row][col+1] = RIGHT
            else:
                new_grid[row][col] = TOP
                new_grid[row+1][col] = BOTTOM
        elif size == 1:
            new_grid[row][col] = CENTER
        
        return new_grid

    def get_possible_actions(self):
        """Returns a list of all possible actions for this Board. An action is a
        ship grid whose ship can be placed in this Board's grid. Prioritizes
        placing bigger ships first"""
        actions = []

        if self.nships_of_size[3] == 0: # We need 1 ship of size 4 placed

            for grid in Board.grids_ship4_hor:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship4_h(row, col):
                    actions.append(grid)
            
            for grid in Board.grids_ship4_ver:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship4_v(row, col):
                    actions.append(grid)

            return actions
        
        elif self.nships_of_size[2] <= 1: # We need 2 ships of size 3 placed

            for grid in Board.grids_ship3_hor:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship3_h(row, col):
                    actions.append(grid)
            
            for grid in Board.grids_ship3_ver:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship3_v(row, col):
                    actions.append(grid)

            return actions
        
        elif self.nships_of_size[1] <= 2: # We need 3 ships of size 2 placed

            for grid in Board.grids_ship2_hor:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship2_h(row, col):
                    actions.append(grid)
            
            for grid in Board.grids_ship2_ver:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship2_v(row, col):
                    actions.append(grid)

            return actions
        
        elif self.nships_of_size[0] <= 3: # We need 4 ships of size 1 placed

            for grid in Board.grids_ship1:
                row = grid[0][0]
                col = grid[0][1]
                if self.can_place_ship1(row, col):
                    actions.append(grid)

            return actions
        else:
            return []

    def interpret_hints(self, nhints: int):
        """Interprets the given hints and does the following things:
        - Creates the puzzle's starting grid and gives it to this Board instance
        - Places any ships of size 1 given in the hints in the starting grid
        - Updates the 'nships_of_size', 'ships_placed_rows' and 
        'ships_placed_cols' lists if a size 1 ship is placed
        - Places water around those ships of size 1
        - Interpreting the hints, puts water on the necessary positions
        - Fills the 'hints_pos' list, that saves each hint's position
        - Creates all possible grids to be added to the starting grid"""

        # hints_matrix is a grid with the hints' ships and water spots placed
        hints_matrix = [[-1] * 10 for _ in range(10)]

        # The starting grid is initially empty
        starting_grid = [[-1 for _ in range(10)] for _ in range(10)]

        # Reads each hint and acts accordingly
        for _ in range(nhints):
            hints_aux = sys.stdin.readline().strip("\n\r")
            hints_aux = hints_aux.split("\t")

            aux = tuple(map(int, hints_aux[1:3]))

            if hints_aux[3] == 'W':
                hints_matrix[aux[0]][aux[1]] = WATER
                starting_grid[aux[0]][aux[1]] = WATER
                Board.hints_pos.append(tuple(map(int, aux)))
            
            elif hints_aux[3] == 'C':
                hints_matrix[aux[0]][aux[1]] = CENTER
                Board.hints_pos.append(tuple(map(int, aux)))

                # If the hint says there is a submarine in this position,
                # then we can instantly put it in the starting grid.
                starting_grid[aux[0]][aux[1]] = CENTER
                self.nships_of_size[0] += 1
                self.ships_placed_cols[aux[1]] += 1
                self.ships_placed_rows[aux[0]] += 1

                if (aux[0]-1) != -1:
                    if (aux[1]-1) != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    starting_grid[aux[0]-1][aux[1]] = WATER
                    if (aux[1]+1) != 10:
                        starting_grid[aux[0]-1][aux[1]+1] = WATER

                if (aux[1]-1) != -1:
                    starting_grid[aux[0]][aux[1]-1] = WATER
                if (aux[1]+1) != 10:
                    starting_grid[aux[0]][aux[1]+1] = WATER

                if (aux[0]+1) != 10:
                    if (aux[1]-1) != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    starting_grid[aux[0]+1][aux[1]] = WATER
                    if (aux[1]+1) != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER

            elif hints_aux[3] == 'T':
                hints_matrix[aux[0]][aux[1]] = TOP
                Board.hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    starting_grid[aux[0]-1][aux[1]] = WATER
                    if aux[1]+1 != 10: 
                        starting_grid[aux[0]-1][aux[1]+1] = WATER

                if aux[1]-1 != -1:
                    starting_grid[aux[0]][aux[1]-1] = WATER
                if aux[1]+1 != 10:
                    starting_grid[aux[0]][aux[1]+1] = WATER

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER
                if aux[0]+2 != 10:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+2][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+2][aux[1]+1] = WATER

            elif hints_aux[3] == 'M':
                hints_matrix[aux[0]][aux[1]] = MIDDLE
                Board.hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]-1][aux[1]+1] = WATER

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER

            elif hints_aux[3] == 'B':
                hints_matrix[aux[0]][aux[1]] = BOTTOM
                Board.hints_pos.append(tuple(map(int, aux)))

                if aux[0]-2 != -1:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-2][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]-2][aux[1]+1] = WATER

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]-1][aux[1]+1] = WATER

                if aux[1]-1 != -1:
                    starting_grid[aux[0]][aux[1]-1] = WATER
                if aux[1]+1 != 10:
                    starting_grid[aux[0]][aux[1]+1] = WATER

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    starting_grid[aux[0]+1][aux[1]] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER
            
            elif hints_aux[3] == 'L':
                hints_matrix[aux[0]][aux[1]] = LEFT
                Board.hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    starting_grid[aux[0]-1][aux[1]] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]-1][aux[1]+1] = WATER
                    if aux[1]+2 != 10:
                        starting_grid[aux[0]-1][aux[1]+2] = WATER

                if aux[1]-1 != -1:
                    starting_grid[aux[0]][aux[1]-1] = WATER

                if aux[0]+1 != 10:
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    starting_grid[aux[0]+1][aux[1]] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER
                    if aux[1]+2 != 10:
                        starting_grid[aux[0]+1][aux[1]+2] = WATER
            
            elif hints_aux[3] == 'R':
                hints_matrix[aux[0]][aux[1]] = RIGHT
                Board.hints_pos.append(tuple(map(int, aux)))

                if aux[0]-1 != -1:
                    if aux[1]-2 != -1:
                        starting_grid[aux[0]-1][aux[1]-2] = WATER
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]-1][aux[1]-1] = WATER
                    starting_grid[aux[0]-1][aux[1]] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]-1][aux[1]+1] = WATER

                if aux[1]+1 != 10:
                    starting_grid[aux[0]][aux[1]+1] = WATER

                if aux[0]+1 != 10:
                    if aux[1]-2 != -1:
                        starting_grid[aux[0]+1][aux[1]-2] = WATER
                    if aux[1]-1 != -1:
                        starting_grid[aux[0]+1][aux[1]-1] = WATER
                    starting_grid[aux[0]+1][aux[1]] = WATER
                    if aux[1]+1 != 10:
                        starting_grid[aux[0]+1][aux[1]+1] = WATER

        self.grid = starting_grid

        create_grids(hints_matrix, self)

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """

        from sys import stdin
        rows_nships = stdin.readline().strip("\n")
        rows_nships = rows_nships.split("\t")
        rows_nships = rows_nships[1:]
        Board.rows_nships = (tuple(map(int, rows_nships)))

        cols_nships = stdin.readline().strip("\n")
        cols_nships = cols_nships.split("\t")
        cols_nships = cols_nships[1:]
        Board.cols_nships = (tuple(map(int, cols_nships)))

        nhints = int(input())

        starting_board = Board([], [], [], [])
        starting_board.interpret_hints(nhints)

        return starting_board

    def __str__(self):
        """Prints this Board's grid in the required format"""

        string_grid = ""

        # Creates a set so that it only needs to iterate through hints_pos once
        hints = set()
        for pos in Board.hints_pos:
            hints.add(pos[0]*10 + pos[1]) # (1,5) = 15, (5,8) = 58, etc

        for row in range(10):
            for col in range(10):

                if self.grid[row][col] == UNKNOWN:
                    if (row*10 + col) in hints:
                        string_grid += "W"
                    else:
                        string_grid += "."

                elif self.grid[row][col] == WATER:
                    if (row*10 + col) in hints:
                        string_grid += "W"
                    else:
                        string_grid += "."
                
                elif self.grid[row][col] == LEFT:
                    if (row*10 + col) in hints:
                        string_grid += "L"
                    else:
                        string_grid += "l"
                
                elif self.grid[row][col] == RIGHT:
                    if (row*10 + col) in hints:
                        string_grid += "R"
                    else:
                        string_grid += "r"

                elif self.grid[row][col] == TOP:
                    if (row*10 + col) in hints:
                        string_grid += "T"
                    else:
                        string_grid += "t"
                
                elif self.grid[row][col] == BOTTOM:
                    if (row*10 + col) in hints:
                        string_grid += "B"
                    else:
                        string_grid += "b"
                
                elif self.grid[row][col] == MIDDLE:
                    if (row*10 + col) in hints:
                        string_grid += "M"
                    else:
                        string_grid += "m"
                
                elif self.grid[row][col] == CENTER:
                    if (row*10 + col) in hints:
                        string_grid += "C"
                    else:
                        string_grid += "c"

                if col == 9 and row != 9:
                    string_grid += "\n"
                    
        return string_grid


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        state = BimaruState(board)
        super().__init__(state)
        pass

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        return state.board.get_possible_actions()

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""

        row = action[0][0]
        col = action[0][1]
        size = action[1]
        orientation = action[2]

        new_grid = state.board.add_ship(action)

        new_nships_of_size = state.board.nships_of_size.copy()
        new_ships_placed_rows = state.board.ships_placed_rows.copy()
        new_ships_placed_cols = state.board.ships_placed_cols.copy()

        new_nships_of_size[size-1] += 1
        new_board = Board(new_grid, new_nships_of_size, new_ships_placed_rows, new_ships_placed_cols)

        if orientation == "hor":
            if size == 4:
                new_board.ships_placed_rows[row] += 4
                new_board.ships_placed_cols[col] += 1
                new_board.ships_placed_cols[col+1] += 1
                new_board.ships_placed_cols[col+2] += 1
                new_board.ships_placed_cols[col+3] += 1

            elif size == 3:
                new_board.ships_placed_rows[row] += 3
                new_board.ships_placed_cols[col] += 1
                new_board.ships_placed_cols[col+1] += 1
                new_board.ships_placed_cols[col+2] += 1

            elif size == 2:
                new_board.ships_placed_rows[row] += 2
                new_board.ships_placed_cols[col] += 1
                new_board.ships_placed_cols[col+1] += 1

            elif size == 1:
                new_board.ships_placed_rows[row] += 1
                new_board.ships_placed_cols[col] += 1

        else: # orientation = "ver"
            if size == 4:
                new_board.ships_placed_rows[row] += 1
                new_board.ships_placed_rows[row+1] += 1
                new_board.ships_placed_rows[row+2] += 1
                new_board.ships_placed_rows[row+3] += 1
                new_board.ships_placed_cols[col] += 4

            elif size == 3:
                new_board.ships_placed_rows[row] += 1
                new_board.ships_placed_rows[row+1] += 1
                new_board.ships_placed_rows[row+2] += 1
                new_board.ships_placed_cols[col] += 3

            elif size == 2:
                new_board.ships_placed_rows[row] += 1
                new_board.ships_placed_rows[row+1] += 1
                new_board.ships_placed_cols[col] += 2

            elif size == 1:
                new_board.ships_placed_rows[row] += 1
                new_board.ships_placed_cols[col] += 1

        return BimaruState(new_board)

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        return state.board.check_objective()

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        #board = node.state.board
        pass


if __name__ == "__main__":
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board = Board.parse_instance()
    bimaru = Bimaru(board)
    goal_node = depth_first_tree_search(bimaru)
    print(goal_node.state.board)

    pass
