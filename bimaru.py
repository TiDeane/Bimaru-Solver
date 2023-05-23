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

import numpy as np

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

def create_grids_ship1(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem circle em todas posições onde pode estar na grid
    # existem no total no maximo 100 combinações diferentes de meter esse ship
    for _ in range(100):
        if rowIndex in starting_board.complete_rows or Board.rows_nships[rowIndex] < 1:
            rowIndex += 1
            columnIndex = 0
            if rowIndex == 10:
                break
            continue

        if columnIndex in starting_board.complete_cols or Board.cols_nships[columnIndex] < 1:
            columnIndex += 1
            if columnIndex == 10:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue
        
        # cria a grid com o barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == CENTER) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN:

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

def create_grids_ship2_horizontal(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 90 combinações diferentes de meter esse ship na horizontal
    for _ in range(90):
        if rowIndex in starting_board.complete_rows or Board.rows_nships[rowIndex] < 2:
            rowIndex += 1
            columnIndex = 0
            if rowIndex == 10:
                break
            continue

        if columnIndex in starting_board.complete_cols or Board.cols_nships[columnIndex] < 1:
            columnIndex += 1
            if columnIndex >= 9:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue
        if (columnIndex+1) in starting_board.complete_cols or Board.cols_nships[columnIndex+1] < 1:
            columnIndex += 2
            if columnIndex >= 9:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue

        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == LEFT) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+1] == UNKNOWN:
            
            if (hints[rowIndex][columnIndex + 1] == UNKNOWN or
                hints[rowIndex][columnIndex + 1] == RIGHT):
                
                grid = [[-1] * 10 for _ in range(10)]
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

def create_grids_ship2_vertical(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem TOP BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 90 combinações diferentes de meter esse ship na vertical
    for _ in range(90):
        if Board.rows_nships[rowIndex] < 1 or rowIndex in starting_board.complete_rows:
            rowIndex += 1
            columnIndex == 0
            if rowIndex >= 10:
                break
            continue
        if Board.rows_nships[rowIndex+1] < 1 or rowIndex+1 in starting_board.complete_rows:
            rowIndex += 2
            columnIndex == 0
            if rowIndex >= 10:
                break
            continue

        if Board.cols_nships[columnIndex] < 2 or columnIndex in starting_board.complete_cols:
            columnIndex += 1
            if columnIndex >= 9:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue

        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == TOP) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+1][columnIndex] == UNKNOWN:
            
            if (hints[rowIndex + 1][columnIndex] == UNKNOWN or
                hints[rowIndex + 1][columnIndex] == BOTTOM):
                
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

def create_grids_ship3_horizontal(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na horizontal
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == LEFT) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+1] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+2] == UNKNOWN:
            
            if (hints[rowIndex][columnIndex + 1] == UNKNOWN or
                hints[rowIndex][columnIndex + 1] == MIDDLE):
                
                if (hints[rowIndex][columnIndex + 2] == UNKNOWN or
                hints[rowIndex][columnIndex + 2] == RIGHT):
                    
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

def create_grids_ship3_vertical(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == TOP) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+1][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+2][columnIndex] == UNKNOWN:
            
            if (hints[rowIndex + 1][columnIndex] == UNKNOWN or
                hints[rowIndex + 1][columnIndex] == MIDDLE):

                if (hints[rowIndex + 2][columnIndex] == UNKNOWN or
                    hints[rowIndex + 2][columnIndex] == BOTTOM):
                    
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

def create_grids_ship4_horizontal(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem LEFT MIDDLE MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 70 combinações diferentes de meter esse ship na horizontal
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == LEFT) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+1] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+2] == UNKNOWN and\
            starting_board.grid[rowIndex][columnIndex+3] == UNKNOWN:
            
            if (hints[rowIndex][columnIndex + 1] == UNKNOWN or
                hints[rowIndex][columnIndex + 1] == MIDDLE):

                if (hints[rowIndex][columnIndex + 2] == UNKNOWN or
                    hints[rowIndex][columnIndex + 2] == MIDDLE):
                    
                    if (hints[rowIndex][columnIndex + 3] == UNKNOWN or
                    hints[rowIndex][columnIndex + 3] == RIGHT):
                        
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

def create_grids_ship4_vertical(hints, starting_board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[rowIndex][columnIndex] == UNKNOWN or
            hints[rowIndex][columnIndex] == TOP) and\
            starting_board.grid[rowIndex][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+1][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+2][columnIndex] == UNKNOWN and\
            starting_board.grid[rowIndex+3][columnIndex] == UNKNOWN:
            
            if (hints[rowIndex + 1][columnIndex] == UNKNOWN or
                hints[rowIndex + 1][columnIndex] == MIDDLE):
                
                if (hints[rowIndex + 2][columnIndex] == UNKNOWN or
                    hints[rowIndex + 2][columnIndex] == MIDDLE):
                    
                    if (hints[rowIndex + 3][columnIndex] == UNKNOWN or
                        hints[rowIndex + 3][columnIndex] == BOTTOM):
                        
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

def create_grids(hints, starting_board):
    """Receives a grid with the ships given in the hints and creates all
    possible grids that can be used to solve the puzzle."""
    Board.grids_ship1 = create_grids_ship1(hints, starting_board)
    Board.grids_ship2_hor = create_grids_ship2_horizontal(hints, starting_board)
    Board.grids_ship2_ver = create_grids_ship2_vertical(hints, starting_board)
    Board.grids_ship3_hor = create_grids_ship3_horizontal(hints, starting_board)
    Board.grids_ship3_ver = create_grids_ship3_vertical(hints, starting_board)
    Board.grids_ship4_hor = create_grids_ship4_horizontal(hints, starting_board)
    Board.grids_ship4_ver = create_grids_ship4_vertical(hints, starting_board)


class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    # Saves the number of ships required in each row and column from 0 to 9
    rows_nships = np.array(10)
    cols_nships = np.array(10)

    # Saves the positions that MUST have ships in the final solution
    hints_pos = []

    # Lists of grids
    grids_ship1 = []
    grids_ship2_hor = []
    grids_ship2_ver = []
    grids_ship3_hor = []
    grids_ship3_ver = []
    grids_ship4_hor = []
    grids_ship4_ver = []

    def __init__(self, grid, nships_of_size):
        self.grid = grid

        # Saves which rows and columns are complete in this Board instance
        self.complete_rows = set()
        self.complete_cols = set()

        # Index 'i' has the number of ships of size i+1 placed in this Board's grid
        if nships_of_size == []:
            self.nships_of_size = np.zeros(4, np.uint8)
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
    
    def can_place_ship(self, row: int, col: int):
        """Returns True if a ship can be placed in the given position"""
        if self.get_value(row, col) != UNKNOWN:
            return False
        
        adj_horizontal = self.adjacent_horizontal_values(row, col)
        adj_vertical = self.adjacent_vertical_values(row, col)
        diagonals_left = self.adjacent_vertical_values(row, col - 1)
        diagonals_right = self.adjacent_vertical_values(row, col + 1)

        for n in range(2): # They are all tuples with 2 values each
            if adj_horizontal[n] > 0 or adj_vertical[n] > 0 or \
                diagonals_left[n] > 0 or diagonals_right[n] > 0:
                return False
        
        return True
    
    def get_row_nships(self, row: int):
        """Returns the number of ships placed in the given row"""
        sum = 0
        if 0 <= row <= 9:
            for col in range(10):
                if self.grid[row][col] > 0:
                    sum += 1
            return sum
        
    def get_col_nships(self, col: int):
        """Returns the number of ships placed in the given column"""
        sum = 0
        if 0 <= col <= 9:
            for row in range(10):
                if self.grid[row][col] > 0:
                    sum += 1
            return sum
    
    def check_close_row(self, row: int):
        """Returns True if the row is complete and False otherwise. If True, it
        also fills the remaining spots with water and adds the row to the
        'complete_rows' set"""
        if 0 <= row <= 9 and self.get_row_nships(row) == Board.rows_nships[row]:
            for col in range(10):
                if self.grid[row][col] == -1:
                    self.grid[row][col] = WATER
            self.complete_rows.add(row)
            return True
        return False
    
    def check_close_col(self, col: int):
        """Returns True if the column is complete and False otherwise. If True,
        it also fills the remaining spots with water and adds the column to the
        'complete_columns' set"""
        if 0 <= col <= 9 and self.get_col_nships(col) == Board.cols_nships[col]:
            for row in range(10):
                if self.grid[row][col] == -1:
                    self.grid[row][col] = WATER
            self.complete_cols.add(col)
            return True
        return False
            
    
    def check_objective(self):
        """Returns True if the Board's grid is the puzzle's solution"""
        for n in range(10):
            if n not in self.complete_rows or n not in self.complete_cols:
                return False
            
        # Maybe hints_matrix could be used for this? (to know what type of ship piece)
        # Try if there's enough memory available
        for pos in self.hints_pos:
            if self.grid[pos[0]][pos[1]] <= 0:
                return False
        
        if self.nships_of_size[0] != 4 or self.nships_of_size[1] != 3 or\
            self.nships_of_size[2] != 2 or self.nships_of_size[3] != 1:
            return False
                
        return True
    
    def get_combined_grid(self, grid):
        """Returns a new grid that is the combination of this Board's grid
        with the grid given as argument"""
        new_grid = [[UNKNOWN for _ in range(10)] for _ in range(10)]
        
        for i in range(10):
            for j in range(10):
                if self.grid[i][j] >= 0 and grid[i][j] == UNKNOWN:
                    new_grid[i][j] = self.grid[i][j]
                elif self.grid[i][j] == UNKNOWN and grid[i][j] >= 0:
                    new_grid[i][j] = grid[i][j]
                else:
                    new_grid[i][j] = self.grid[i][j]
        
        return new_grid

    def get_possible_actions(self):
        #TODO
        actions = []

        hor_positions = []
        ver_positions = []

        if self.nships_of_size[3] == 0: # We need 1 ship of size 4 placed

            for rowIndex in range(10):
                for colIndex in range(10):
                    if colIndex <= 6 and self.can_place_ship(rowIndex, colIndex)\
                            and self.can_place_ship(rowIndex, colIndex+1)\
                            and self.can_place_ship(rowIndex, colIndex+2)\
                            and self.can_place_ship(rowIndex, colIndex+3):
                        hor_positions.append((rowIndex,colIndex))

                    if rowIndex <= 6 and self.can_place_ship(rowIndex, colIndex)\
                            and self.can_place_ship(rowIndex+1, colIndex)\
                            and self.can_place_ship(rowIndex+2, colIndex)\
                            and self.can_place_ship(rowIndex+3, colIndex):
                        ver_positions.append((rowIndex,colIndex))

            for i in range(len(Board.grids_ship4_hor)):
                for pos in hor_positions:
                    if Board.grids_ship4_hor[i][pos[0]][pos[1]] == LEFT\
                            and Board.grids_ship4_hor[i][pos[0]][pos[1]+1] == MIDDLE\
                            and Board.grids_ship4_hor[i][pos[0]][pos[1]+2] == MIDDLE\
                            and Board.grids_ship4_hor[i][pos[0]][pos[1]+3] == RIGHT:
                        actions.append((Board.grids_ship4_hor[i], 4))
            for i in range(len(Board.grids_ship4_ver)):
                for pos in ver_positions:
                    if Board.grids_ship4_ver[i][pos[0]][pos[1]] == TOP\
                            and Board.grids_ship4_ver[i][pos[0]+1][pos[1]] == MIDDLE\
                            and Board.grids_ship4_ver[i][pos[0]+2][pos[1]] == MIDDLE\
                            and Board.grids_ship4_ver[i][pos[0]+3][pos[1]] == BOTTOM:
                        actions.append((Board.grids_ship4_ver[i], 4))

            return actions
        elif self.nships_of_size[2] <= 1: # We need 2 ships of size 3 placed
            # search for all positions for a ship of size 3
            # iterate through the grids and check if any of those positions (and the next 2) are occupied (the ship is there)
            # add those grids
            # do this for horizontal and then for vertical
            return actions
        elif self.nships_of_size[1] <= 2: # We need 3 ships of size 2 placed
            # search for all positions for a ship of size 2
            # iterate through the grids and check if any of those positions (and the next one) are occupied (the ship is there)
            # add those grids
            # do this for horizontal and then for vertical
            return actions
        elif self.nships_of_size[0] <= 3: # We need 4 ships of size 1 placed
            # search for all positions for a ship of size 1
            # iterate through the grids and check if any of those positions are occupied (the ship is there)
            # add those grids
            return actions
        else:
            return []

    def interpret_hints(self, nhints: int):
        """Interprets the given hints and does the following things:
        - Creates the puzzle's starting grid
        - Places any ships of size 1 given in the hints in the starting grid
        - Places water around those ships of size 1
        - Reading the hints, puts water on the necessary positions
        - Checks if any rows or columns have already been completed. If so, adds
        them to the corresponding sets and fills the remaining spots with water
        - Creates all possible grids to be added to the starting grid"""

        hints_matrix = np.array([[-1] * 10 for _ in range(10)])
        starting_grid = [[-1 for _ in range(10)] for _ in range(10)]

        for _ in range(nhints):
            hints_aux = sys.stdin.readline().strip("\n\r")
            hints_aux = hints_aux.split("\t")

            aux = tuple(map(int, hints_aux[1:3]))

            match hints_aux[3]:
                case 'W':
                    hints_matrix[aux[0]][aux[1]] = WATER
                    starting_grid[aux[0]][aux[1]] = WATER
                case 'C':
                    hints_matrix[aux[0]][aux[1]] = CENTER
                    Board.hints_pos.append(tuple(map(int, aux)))

                    # If the hint says there is a submarine in this position,
                    # then we can instantly put it in the starting grid.
                    starting_grid[aux[0]][aux[1]] = CENTER
                    self.nships_of_size[0] += 1

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
                case 'T':
                    hints_matrix[aux[0]][aux[1]] = TOP
                    hints_matrix[aux[0]+1][aux[1]] = MIDDLE
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
                case 'M':
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
                case 'B':
                    hints_matrix[aux[0]][aux[1]] = BOTTOM
                    hints_matrix[aux[0]-1][aux[1]] = MIDDLE
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
                case 'L':
                    hints_matrix[aux[0]][aux[1]] = LEFT
                    hints_matrix[aux[0]][aux[1]+1] = MIDDLE
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
                case 'R':
                    hints_matrix[aux[0]][aux[1]] = RIGHT
                    hints_matrix[aux[0]][aux[1]-1] = MIDDLE
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
        
        for n in range(10):
            self.check_close_col(n)
            self.check_close_row(n)

        #print("hints_pos:\n", Board.hints_pos)
        
        #print("Hints matrix:\n", np.array(hints_matrix))

        #print("Starting grid:\n", np.array(starting_grid))

        #print("Ships per row: \n", Board.rows_nships)
        #print("Ships per columnn: \n", Board.cols_nships)

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

        starting_board = Board([], [])
        starting_board.interpret_hints(nhints)

        return starting_board

    def __str__(self): #TODO
        """When printing a class, this function gets called.
        #TODO Make it print the grid's representation, please"""
        pass


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        state = BimaruState(board)
        super().__init__(state)

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        return state.board.get_possible_actions()

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        #TODO

        new_grid = state.board.get_combined_grid(action[0])
        new_board = Board(new_grid, state.board.nships_of_size)
        new_state = BimaruState(new_board)
        new_state.board.nships_of_size[action[1]-1] += 1

        return new_state

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        return state.board.check_objective()

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # Quantos barcos falta colocar? Exemplo:
        return 10 - sum(self.nships_of_size)
        # return sum(self.nships_of_size), se darem prioridade ao maior número

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board = Board.parse_instance()
    bimaru = Bimaru(board)
    #goal_node = breadth_first_tree_search(bimaru)
    #print(goal_node)

    pass
