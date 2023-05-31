"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ 
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ 
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ 
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ 
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ 
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ 
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ 
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ 
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

""" delete later """

import numpy as np
import sys

# "defines"
UNKNOWN = -1
WATER = 0
LEFT = 1
RIGHT = 2
TOP = 3
BOTTOM = 4
MIDDLE = 5
CENTER = 6

def is_left_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == LEFT) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != MIDDLE) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != LEFT) and\
        (columnIndex < 2 or board[rowIndex][columnIndex - 2] != LEFT) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != MIDDLE) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != MIDDLE) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != TOP) and\
        (rowIndex < 2 or board[rowIndex - 2][columnIndex] != TOP) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != BOTTOM) and\
        (rowIndex > 7 or board[rowIndex + 2][columnIndex] != BOTTOM):
            return True
    else:
        return False

def is_right_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == CENTER) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != MIDDLE) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != RIGHT) and\
        (columnIndex > 7 or board[rowIndex][columnIndex + 2] != RIGHT) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != MIDDLE) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != MIDDLE) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != TOP) and\
        (rowIndex < 2 or board[rowIndex - 2][columnIndex] != TOP) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != BOTTOM) and\
        (rowIndex > 7 or board[rowIndex + 2][columnIndex] != BOTTOM):
            return True
    else:
        return False

def is_top_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == TOP) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != MIDDLE) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != MIDDLE) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != LEFT) and\
        (columnIndex < 2 or board[rowIndex][columnIndex - 2] != LEFT) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != RIGHT) and\
        (columnIndex > 7 or board[rowIndex][columnIndex + 2] != RIGHT) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != MIDDLE) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != TOP) and\
        (rowIndex < 2 or board[rowIndex - 2][columnIndex] != TOP):
            return True
    else:
        return False

def is_bottom_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == BOTTOM) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != MIDDLE) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != MIDDLE) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != LEFT) and\
        (columnIndex < 2 or board[rowIndex][columnIndex - 2] != LEFT) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != RIGHT) and\
        (columnIndex > 7 or board[rowIndex][columnIndex + 2] != RIGHT) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != MIDDLE) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != BOTTOM) and\
        (rowIndex > 7 or board[rowIndex + 2][columnIndex] != BOTTOM):
            return True
    else:
        return False

def is_middle_hor_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == MIDDLE) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != TOP) and\
        (rowIndex < 2 or board[rowIndex - 2][columnIndex] != TOP) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != BOTTOM) and\
        (rowIndex > 7 or board[rowIndex + 2][columnIndex] != BOTTOM):
            return True
    else:
        return False
    
def is_middle_ver_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == MIDDLE) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != LEFT) and\
        (columnIndex < 2 or board[rowIndex][columnIndex - 2] != LEFT) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != RIGHT) and\
        (columnIndex > 7 or board[rowIndex][columnIndex + 2] != RIGHT):
            return True
    else:
        return False

def is_center_possible(columnIndex, rowIndex, board):
    if (board[rowIndex][columnIndex] == UNKNOWN or
        board[rowIndex][columnIndex] == CENTER) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != MIDDLE) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != MIDDLE) and\
        (columnIndex < 1 or board[rowIndex][columnIndex - 1] != LEFT) and\
        (columnIndex < 2 or board[rowIndex][columnIndex - 2] != LEFT) and\
        (columnIndex > 8 or board[rowIndex][columnIndex + 1] != RIGHT) and\
        (columnIndex > 7 or board[rowIndex][columnIndex + 2] != RIGHT) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != MIDDLE) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != MIDDLE) and\
        (rowIndex < 1 or board[rowIndex - 1][columnIndex] != TOP) and\
        (rowIndex < 2 or board[rowIndex - 2][columnIndex] != TOP) and\
        (rowIndex > 8 or board[rowIndex + 1][columnIndex] != BOTTOM) and\
        (rowIndex > 7 or board[rowIndex + 2][columnIndex] != BOTTOM):
            return True
    else:
        return False


def create_grids_ship1(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem circle em todas posições onde pode estar na grid
    # existem no total no maximo 100 combinações diferentes de meter esse ship
    for _ in range(100):
        # cria a grid com o barco
        if is_center_possible(columnIndex, rowIndex, board):

            grid = [[-1] * 10 for _ in range(10)]
            grid[rowIndex][columnIndex] = CENTER
            # desenha agua em cima do barco
            if rowIndex > 0:
                for auxColumnIndex in range(columnIndex - 1, columnIndex + 2):
                    if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                        grid[rowIndex - 1][auxColumnIndex] = WATER
            # desneha agua em baixo do barco
            if rowIndex < 9:
                for auxColumnIndex in range(columnIndex - 1, columnIndex + 2):
                    if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                        grid[rowIndex + 1][auxColumnIndex] = WATER
            # desenha a agua a esquerda e a direita do barco
            if columnIndex > 0:
                grid[rowIndex][columnIndex - 1] = WATER
            if columnIndex < 9:
                grid[rowIndex][columnIndex + 1] = WATER
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
        if is_left_possible(columnIndex, rowIndex, board):
            
            if is_left_possible(columnIndex + 1, rowIndex, board):
                
                grid = [[-1] * 10 for _ in range(10)]
                # desenha o barco
                grid[rowIndex][columnIndex] = LEFT
                grid[rowIndex][columnIndex + 1] = RIGHT
                # desenha agua em cima do barco
                if rowIndex > 0:
                    for auxColumnIndex in range(columnIndex - 1, columnIndex + 3):
                        if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                            grid[rowIndex - 1][auxColumnIndex] = WATER
                # desneha agua em baixo do barco
                if rowIndex < 9:
                    for auxColumnIndex in range(columnIndex - 1, columnIndex + 3):
                        if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                            grid[rowIndex + 1][auxColumnIndex] = WATER
                # desenha a agua a esquerda e a direita do barco
                if columnIndex > 0:
                    grid[rowIndex][columnIndex - 1] = WATER
                if (columnIndex + 1) < 9:
                    grid[rowIndex][columnIndex + 2] = WATER
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
        if is_top_possible(columnIndex, rowIndex, board):
            
            if is_bottom_possible(columnIndex, rowIndex + 1, board):
                
                grid = [[-1] * 10 for _ in range(10)]
                grid[rowIndex][columnIndex] = TOP
                grid[rowIndex + 1][columnIndex] = BOTTOM
                # desenha agua do lado esquerdo do barco
                if columnIndex > 0:
                    for auxRowIndex in range(rowIndex - 1, rowIndex + 3):
                        if auxRowIndex >= 0 and auxRowIndex <= 9:
                            grid[auxRowIndex][columnIndex - 1] = WATER
                # desenha agua do lado direito do barco
                if columnIndex < 9:
                    for auxRowIndex in range(rowIndex - 1, rowIndex + 3):
                        if auxRowIndex >= 0 and auxRowIndex <= 9:
                            grid[auxRowIndex][columnIndex + 1] = WATER
                # desenha agua em cima e em baixo do barco
                if rowIndex > 0:
                    grid[rowIndex - 1][columnIndex] = WATER
                if (rowIndex + 1) < 9:
                    grid[rowIndex + 2][columnIndex] = WATER
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
        if is_left_possible(columnIndex, rowIndex, board):
            
            if is_middle_hor_possible(columnIndex + 1, rowIndex, board):
                
                if is_right_possible(columnIndex + 2, rowIndex, board):
                    
                    grid = [[-1] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = LEFT
                    grid[rowIndex][columnIndex + 1] = MIDDLE
                    grid[rowIndex][columnIndex + 2] = RIGHT
                    # desenha agua em cima do barco
                    if rowIndex > 0:
                        for auxColumnIndex in range(columnIndex - 1, columnIndex + 4):
                            if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                                grid[rowIndex - 1][auxColumnIndex] = WATER
                    # desneha agua em baixo barco
                    if rowIndex < 9:
                        for auxColumnIndex in range(columnIndex - 1, columnIndex + 4):
                            if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                                grid[rowIndex + 1][auxColumnIndex] = WATER
                    # desenha a agua a esquerda e a direita do barco
                    if columnIndex > 0:
                        grid[rowIndex][columnIndex - 1] = WATER
                    if (columnIndex + 2) < 9:
                        grid[rowIndex][columnIndex + 3] = WATER
                    grids.append(grid)
                else:
                    if board[rowIndex][columnIndex + 2] != MIDDLE:
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
        if is_top_possible(columnIndex, rowIndex, board):
            
            if is_middle_ver_possible(columnIndex, rowIndex + 1, board):

                if is_bottom_possible(columnIndex, rowIndex + 2, board):
                    
                    grid = [[-1] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = TOP
                    grid[rowIndex + 1][columnIndex] = MIDDLE
                    grid[rowIndex + 2][columnIndex] = BOTTOM
                    # desenha agua do lado esquerdo do barco
                    if columnIndex > 0:
                        for auxRowIndex in range(rowIndex - 1, rowIndex + 4):
                            if auxRowIndex >= 0 and auxRowIndex <= 9:
                                grid[auxRowIndex][columnIndex - 1] = WATER
                    # desenha agua do lado direito do barco
                    if columnIndex < 9:
                        for auxRowIndex in range(rowIndex - 1, rowIndex + 4):
                            if auxRowIndex >= 0 and auxRowIndex <= 9:
                                grid[auxRowIndex][columnIndex + 1] = WATER
                    # desenha agua em cima e em baixo do barco
                    if rowIndex > 0:
                        grid[rowIndex - 1][columnIndex] = WATER
                    if (rowIndex + 2) < 9:
                        grid[rowIndex + 3][columnIndex] = WATER
                    grids.append(grid)
                else:
                    if board[rowIndex][columnIndex + 2] != MIDDLE:
                        columnIndex += 2
            else:
                columnIndex += 1

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
        if is_left_possible(columnIndex, rowIndex, board):
            
            if is_middle_hor_possible(columnIndex + 1, rowIndex, board):

                if is_middle_hor_possible(columnIndex + 2, rowIndex, board):
                    
                    if is_right_possible(columnIndex + 3, rowIndex, board):
                        
                        grid = [[-1] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = LEFT
                        grid[rowIndex][columnIndex + 1] = MIDDLE
                        grid[rowIndex][columnIndex + 2] = MIDDLE
                        grid[rowIndex][columnIndex + 3] = RIGHT
                        # desenha agua em cima do barco
                        if rowIndex > 0:
                            for auxColumnIndex in range(columnIndex - 1, columnIndex + 5):
                                if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                                    grid[rowIndex - 1][auxColumnIndex] = WATER
                        # desneha agua em baixo do barco
                        if rowIndex < 9:
                            for auxColumnIndex in range(columnIndex - 1, columnIndex + 5):
                                if auxColumnIndex >= 0 and auxColumnIndex <= 9:
                                    grid[rowIndex + 1][auxColumnIndex] = WATER
                        # desenha a agua a esquerda e a direita do barco
                        if columnIndex > 0:
                            grid[rowIndex][columnIndex - 1] = WATER
                        if (columnIndex + 3) < 9:
                            grid[rowIndex][columnIndex + 4] = WATER
                        grids.append(grid)
                    else:
                        if board[rowIndex][columnIndex + 3] != MIDDLE:
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
        if is_top_possible(columnIndex, rowIndex, board):
            
            if is_middle_ver_possible(columnIndex, rowIndex + 1, board):
                
                if is_middle_ver_possible(columnIndex, rowIndex + 2, board):
                    
                    if is_bottom_possible(columnIndex, rowIndex + 3, board):
                        
                        grid = [[-1] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = TOP
                        grid[rowIndex + 1][columnIndex] = MIDDLE
                        grid[rowIndex + 2][columnIndex] = MIDDLE
                        grid[rowIndex + 3][columnIndex] = BOTTOM
                        # desenha agua do lado esquerdo do barco
                        if columnIndex > 0:
                            for auxRowIndex in range(rowIndex - 1, rowIndex + 5):
                                if auxRowIndex >= 0 and auxRowIndex <= 9:
                                    grid[auxRowIndex][columnIndex - 1] = WATER
                        # desenha agua do lado direito do barco
                        if columnIndex < 9:
                            for auxRowIndex in range(rowIndex - 1, rowIndex + 5):
                                if auxRowIndex >= 0 and auxRowIndex <= 9:
                                    grid[auxRowIndex][columnIndex + 1] = WATER
                        # desenha agua em cima e em baixo do barco
                        if rowIndex > 0:
                            grid[rowIndex - 1][columnIndex] = WATER
                        if (rowIndex + 3) < 9:
                            grid[rowIndex + 3][columnIndex] = WATER

                        grids.append(grid)
                    else:
                        if board[rowIndex + 3][columnIndex] != MIDDLE:
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
    for grid in grids:
        print_grid(grid)
        print()

def print_grid(grid):
    linha = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] != -1:
                print(" ", end="")
            print(grid[i][j], end="")
        print(" linha: " + str(linha))
        linha += 1

""" UNKNOWN = -1, WATER = 0, LEFT = 1, RIGHT = 2, TOP = 3, BOTTOM = 4, MIDDLE = 5, CENTER = 6 """
"""
starting_board = [
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER]
]
"""
starting_board = [
    [WATER, LEFT, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [WATER, WATER, WATER, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN]
]

instance03 = [
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, WATER],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, WATER, WATER, CENTER],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, TOP, WATER, WATER],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, UNKNOWN, WATER, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, UNKNOWN, WATER, WATER, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, BOTTOM, WATER, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, WATER, UNKNOWN, WATER, WATER, WATER, WATER, UNKNOWN, UNKNOWN, UNKNOWN],
    [UNKNOWN, UNKNOWN, MIDDLE, UNKNOWN, WATER, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN],
    [WATER, WATER, WATER, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, WATER, UNKNOWN, UNKNOWN],
    [WATER, CENTER, WATER, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN]
]


#print_all_grids(create_grids_ship1(starting_board))

#print_all_grids(create_grids_ship2_horizontal(starting_board))

#print_all_grids(create_grids_ship2_vertical(starting_board))

#print_all_grids(create_grids_ship3_horizontal(starting_board))

#print_all_grids(create_grids_ship3_vertical(starting_board))

#print_all_grids(create_grids_ship4_horizontal(starting_board))

#print_all_grids(create_grids_ship4_vertical(starting_board))

print_all_grids(create_grids(instance03))