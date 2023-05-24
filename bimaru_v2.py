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
    row = 0
    col = 0

    # poem circle em todas posições onde pode estar na grid
    # existem no total no maximo 100 combinações diferentes de meter esse ship
    for _ in range(100):
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col == 10:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        
        # cria a grid com o barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == CENTER) and\
            starting_board.grid[row][col] == UNKNOWN:

            grid = ((row, col), 1, "hor")

            grids.append(grid)

        # proximo ponto
        col += 1
        if col == 10:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break

    return grids

def create_grids_ship2_horizontal(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem LEFT RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 90 combinações diferentes de meter esse ship na horizontal
    for _ in range(90):
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

        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]:
            col += 1
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue
        if starting_board.ships_placed_cols[col+1] == Board.cols_nships[col+1]:
            col += 2
            if col >= 9:
                col = 0
                row += 1
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == LEFT) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row][col+1] == UNKNOWN:
            
            if (hints[row][col + 1] == UNKNOWN or
                hints[row][col + 1] == RIGHT):
                
                grid = ((row, col), 2, "hor")

                grids.append(grid)
            else:
                col += 1

        # proximo ponto
        col += 1
        if col >= 9:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break

    return grids

def create_grids_ship2_vertical(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem TOP BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 90 combinações diferentes de meter esse ship na vertical
    for _ in range(90):
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]\
                or Board.cols_nships[col] < 2\
                or starting_board.ships_placed_cols[col] + 2 > Board.cols_nships[col]:
            col += 1
            row = 0
            # Não existe mais nenhum ponto
            if col == 10:
                break
            continue
        
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

        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (hints[row][col] == UNKNOWN or
            hints[row][col] == TOP) and\
            starting_board.grid[row][col] == UNKNOWN and\
            starting_board.grid[row+1][col] == UNKNOWN:
            
            if (hints[row + 1][col] == UNKNOWN or
                hints[row + 1][col] == BOTTOM):
                
                grid = ((row, col), 2, "ver")

                grids.append(grid)
            else:
                row += 1

        # proximo ponto
        row += 1
        if row >= 9:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
                break

    return grids

def create_grids_ship3_horizontal(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem LEFT MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na horizontal
    for _ in range(80):
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row]\
                or Board.rows_nships[row] < 3\
                or starting_board.ships_placed_rows[row] + 3 > Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

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

        # cria a grid com o barco se for uma posição onde possa haver esse barco
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

                    grids.append(grid)
                else:
                    col += 2
            else:
                col += 1

        # proximo ponto
        col += 1
        if col >= 8:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break

    return grids

def create_grids_ship3_vertical(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(80):
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col]\
                or Board.cols_nships[col] < 3\
                or starting_board.ships_placed_cols[col]+3 > Board.cols_nships[col]:
            col += 1
            row = 0
            if col == 10:
                break
            continue

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
        
        # cria a grid com o barco se for uma posição onde possa haver esse barco
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
                    
                    grids.append(grid)
                else:
                    row += 2
            else:
                row += 1

        # proximo ponto
        row += 1
        if row >= 8:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
                break

    return grids

def create_grids_ship4_horizontal(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem LEFT MIDDLE MIDDLE RIGHT em todas posições onde pode estar na grid
    # existem no total no maximo 70 combinações diferentes de meter esse ship na horizontal
    for _ in range(70):
        if starting_board.ships_placed_rows[row] == Board.rows_nships[row] or Board.rows_nships[row] < 4\
                or starting_board.ships_placed_rows[row] + 4 > Board.rows_nships[row]:
            row += 1
            col = 0
            if row == 10:
                break
            continue

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

        # cria a grid com o barco se for uma posição onde possa haver esse barco
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
                        
                        grids.append(grid)
                    else:
                        col += 3
                else:
                    col += 2
            else:
                col += 1

        # proximo ponto
        col += 1
        if col >= 7:
            col = 0
            row += 1
            # Não existe mais nenhum ponto
            if row == 10:
                break

    return grids

def create_grids_ship4_vertical(hints, starting_board):
    grids = []
    row = 0
    col = 0

    # poem TOP MIDDLE BOTTOM em todas posições onde pode estar na grid
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(70):
        if starting_board.ships_placed_cols[col] == Board.cols_nships[col] or Board.cols_nships[col] < 4\
                or starting_board.ships_placed_cols[col] + 4 > Board.cols_nships[col]:
            col += 1
            if col == 10:
                row += 1
                col = 0
                # Não existe mais nenhum ponto
                if row == 10:
                    break
            continue

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

        # cria a grid com o barco se for uma posição onde possa haver esse barco
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
                        
                        grids.append(grid)
                    else:
                        row += 3
                else:
                    row += 2
            else:
                row += 1

        # proximo ponto
        row += 1
        if row >= 7:
            row = 0
            col += 1
            # Não existe mais nenhum ponto
            if col == 10:
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

        # ships_placed_rows[n] holds how many ships have been placed in row n
        if len(ships_placed_rows) == 0:
            self.ships_placed_rows = np.zeros(10, np.uint8)
        else:
            self.ships_placed_rows = ships_placed_rows
        
        # ships_placed_cols[n] holds how many ships have been placed in column n
        if len(ships_placed_cols) == 0:
            self.ships_placed_cols = np.zeros(10, np.uint8)
        else:
            self.ships_placed_cols = ships_placed_cols

        # Index 'i' has the number of ships of size i+1 placed in this Board's grid
        if len(nships_of_size) == 0:
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
    
    def no_ships_around(self, row: int, col: int):
        """Returns True if a ship can be placed in the given position"""

        adj_horizontal = self.adjacent_horizontal_values(row, col)
        adj_vertical = self.adjacent_vertical_values(row, col)
        diagonals_left = self.adjacent_vertical_values(row, col - 1)
        diagonals_right = self.adjacent_vertical_values(row, col + 1)

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
        
        return self.no_ships_around(row, col) and self.no_ships_around(row, col+1) and self.no_ships_around(row, col+2)
    
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
        
        return self.no_ships_around(row, col) and self.no_ships_around(row+1, col) and self.no_ships_around(row+2, col)
    
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
        print(self.ships_placed_rows)  #TODO remove these prints
        print(Board.rows_nships)
        print(self.ships_placed_cols)
        print(Board.cols_nships)
        # Checks if all rows and columns have the required number of ships
        for n in range(10):
            if self.ships_placed_rows[n] != Board.rows_nships[n] or\
                    self.ships_placed_cols[n] != Board.cols_nships[n]:
                return False

        # Checks if all hint position have ships in them
        for pos in self.hints_pos:
            if self.grid[pos[0]][pos[1]] == -1:
                return False
        
        # Checks if there are 4 size 1 ships, 3 size 2 ships,
        # 2 size 3 ships and 1 size 4 ship
        if self.nships_of_size[0] != 4 or self.nships_of_size[1] != 3 or\
            self.nships_of_size[2] != 2 or self.nships_of_size[3] != 1:
            return False
                
        return True
    
    def add_ship(self, ship_grid):
        """Returns a new 10x10 grid that is the combination of this Board's grid
        and the ship grid given as argument"""
        new_grid = [row[:] for row in self.grid] # hard copy of this board's grid

        size = ship_grid[1]
        orientation = ship_grid[2]
        row = ship_grid[0][0]
        col = ship_grid[0][1]
        
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
        actions = []

        if self.nships_of_size[3] == 0: # We need 1 ship of size 4 placed

            for i in range(len(Board.grids_ship4_hor)):
                row = Board.grids_ship4_hor[i][0][0]
                col = Board.grids_ship4_hor[i][0][1]
                if self.can_place_ship4_h(row, col):
                    actions.append(Board.grids_ship4_hor[i])
            for i in range(len(Board.grids_ship4_ver)):
                row = Board.grids_ship4_ver[i][0][0]
                col = Board.grids_ship4_ver[i][0][1]
                if self.can_place_ship4_v(row, col):
                    actions.append(Board.grids_ship4_ver[i])

            return actions
        
        elif self.nships_of_size[2] <= 1: # We need 2 ships of size 3 placed
            
            for i in range(len(Board.grids_ship3_hor)):
                row = Board.grids_ship3_hor[i][0][0]
                col = Board.grids_ship3_hor[i][0][1]
                if self.can_place_ship3_h(row, col):
                    actions.append(Board.grids_ship3_hor[i])
            for i in range(len(Board.grids_ship3_ver)):
                row = Board.grids_ship3_ver[i][0][0]
                col = Board.grids_ship3_ver[i][0][1]
                if self.can_place_ship3_v(row, col):
                    actions.append(Board.grids_ship3_ver[i])

            return actions
        
        elif self.nships_of_size[1] <= 2: # We need 3 ships of size 2 placed

            for i in range(len(Board.grids_ship2_hor)):
                row = Board.grids_ship2_hor[i][0][0]
                col = Board.grids_ship2_hor[i][0][1]
                if self.can_place_ship2_h(row, col):
                    actions.append(Board.grids_ship2_hor[i])
            for i in range(len(Board.grids_ship2_ver)):
                row = Board.grids_ship2_ver[i][0][0]
                col = Board.grids_ship2_ver[i][0][1]
                if self.can_place_ship2_v(row, col):
                    actions.append(Board.grids_ship2_ver[i])

            return actions
        
        elif self.nships_of_size[0] <= 3: # We need 4 ships of size 1 placed

            for i in range(len(Board.grids_ship1)):
                row = Board.grids_ship1[i][0][0]
                col = Board.grids_ship1[i][0][1]
                if self.can_place_ship1(row, col):
                    actions.append(Board.grids_ship1[i])

            return actions
        else:
            return []

    def interpret_hints(self, nhints: int):
        """Interprets the given hints and does the following things:
        - Creates the puzzle's starting grid and gives it to this Board
        - Places any ships of size 1 given in the hints in the starting grid
        - Updates the 'nships_of_size', 'ships_placed_rows' and 
        'ships_placed_cols' lists if a size 1 ship is placed
        - Places water around those ships of size 1
        - Reading the hints, puts water on the necessary positions
        - Fills the 'hints_pos' list, that saves each hint's position
        - Creates all possible grids to be added to the starting grid"""

        # A matrix with the hints' ships and water spots placed
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
                    Board.hints_pos.append(tuple(map(int, aux)))
                case 'C':
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
                case 'T':
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

        print("hints_pos:\n", Board.hints_pos)
        
        print("Hints matrix:\n", np.array(hints_matrix))

        print("Starting grid:\n", np.array(self.grid))
        print("Starting grid:\n", self)

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

    def __str__(self): #TODO
        """Prints this Board's grid in the required format"""

        string_grid = ""

        hints = []
        for pos in Board.hints_pos:
            hints.append(pos[0]*10 + pos[1]) # (1,5) = 15, (5,8) = 58, etc

        for row in range(10):
            for col in range(10):
                match self.grid[row][col]:
                    case -1:
                        if (row*10 + col) in hints:
                            string_grid += "W"
                        else:
                            string_grid += "."
                    case 0:
                        if (row*10 + col) in hints:
                            string_grid += "W"
                        else:
                            string_grid += "."
                    case 1:
                        if (row*10 + col) in hints:
                            string_grid += "L"
                        else:
                            string_grid += "l"
                    case 2:
                        if (row*10 + col) in hints:
                            string_grid += "R"
                        else:
                            string_grid += "r"
                    case 3:
                        if (row*10 + col) in hints:
                            string_grid += "T"
                        else:
                            string_grid += "t"
                    case 4:
                        if (row*10 + col) in hints:
                            string_grid += "B"
                        else:
                            string_grid += "b"
                    case 5:
                        if (row*10 + col) in hints:
                            string_grid += "M"
                        else:
                            string_grid += "m"
                    case 6:
                        if (row*10 + col) in hints:
                            string_grid += "C"
                        else:
                            string_grid += "c"
                if col == 9:
                    string_grid += "\n"
        return string_grid


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
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
        #TODO

        row = action[0][0]
        col = action[0][1]
        size = action[1]
        orientation = action[2]

        new_grid = state.board.add_ship(action)
        new_board = Board(new_grid, state.board.nships_of_size,\
                    state.board.ships_placed_rows, state.board.ships_placed_cols)
        new_board.nships_of_size[action[1]-1] += 1

        if orientation == "hor":
            match size:
                case 4:
                    new_board.ships_placed_rows[row] += 4
                    new_board.ships_placed_cols[col] += 1
                    new_board.ships_placed_cols[col+1] += 1
                    new_board.ships_placed_cols[col+2] += 1
                    new_board.ships_placed_cols[col+3] += 1
                    
                case 3:
                    new_board.ships_placed_rows[row] += 3
                    new_board.ships_placed_cols[col] += 1
                    new_board.ships_placed_cols[col+1] += 1
                    new_board.ships_placed_cols[col+2] += 1

                case 2:
                    new_board.ships_placed_rows[row] += 2
                    new_board.ships_placed_cols[col] += 1
                    new_board.ships_placed_cols[col+1] += 1

                case 1:
                    new_board.ships_placed_rows[row] += 1
                    new_board.ships_placed_cols[col] += 1

        else: # orientation = "ver"
            match size:
                case 4:
                    new_board.ships_placed_rows[row] += 1
                    new_board.ships_placed_rows[row+1] += 1
                    new_board.ships_placed_rows[row+2] += 1
                    new_board.ships_placed_rows[row+3] += 1
                    new_board.ships_placed_cols[col] += 4

                case 3:
                    new_board.ships_placed_rows[row] += 1
                    new_board.ships_placed_rows[row+1] += 1
                    new_board.ships_placed_rows[row+2] += 1
                    new_board.ships_placed_cols[col] += 3

                case 2:
                    new_board.ships_placed_rows[row] += 1
                    new_board.ships_placed_rows[row+1] += 1
                    new_board.ships_placed_cols[col] += 2

                case 1:
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
    #goal_node = depth_first_tree_search(bimaru)
    #print(goal_node.state.board)

    s1 = BimaruState(board)
    actions = s1.board.get_possible_actions()
    print(actions)
    s2 = bimaru.result(s1, actions[3])
    print(s2.board)
    actions = s2.board.get_possible_actions()
    print(actions)
    s3 = bimaru.result(s2, actions[2])
    print(s3.board)
    actions = s3.board.get_possible_actions()
    print(actions)
    s4 = bimaru.result(s3, actions[0])
    print(s4.board)
    actions = s4.board.get_possible_actions()
    print(actions)
    s5 = bimaru.result(s4, actions[2])
    print(s5.board)
    actions = s5.board.get_possible_actions()
    print(actions)
    s6 = bimaru.result(s5, actions[1])
    print(s6.board)
    actions = s6.board.get_possible_actions()
    print(actions)
    s7 = bimaru.result(s6, actions[0])
    print(s7.board)
    actions = s7.board.get_possible_actions()
    print(actions)
    s8 = bimaru.result(s7, actions[0])
    print(s8.board)
    actions = s8.board.get_possible_actions()
    print(actions)
    s9 = bimaru.result(s8, actions[0])
    print(s9.board)
    actions = s9.board.get_possible_actions()
    print(actions)

    print(s9.board.check_objective())

    pass
