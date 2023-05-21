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

def create_grids_ship1(board):
    grids = []
    rowIndex = 0
    columnIndex = 0

    # poem circle em todas posições onde pode estar na grid
    # existem no total no maximo 100 combinações diferentes de meter esse ship
    for _ in range(100):
        # cria a grid com o barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == CENTER) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1:

            grid = [[-1] * 10 for _ in range(10)]
            grid[rowIndex][columnIndex] = CENTER

            """
            grid[rowIndex-1][columnIndex-1] = WATER
            grid[rowIndex-1][columnIndex] = WATER
            grid[rowIndex-1][columnIndex+1] = WATER
            grid[rowIndex][columnIndex-1] = WATER
            grid[rowIndex][columnIndex+1] = WATER
            grid[rowIndex+1][columnIndex-1] = WATER
            grid[rowIndex+1][columnIndex] = WATER
            grid[rowIndex+1][columnIndex+1] = WATER"""

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
    # existem no total no maximo 90 combinações diferentes de meter esse ship na horizontal
    for _ in range(90):
        if Board.rows_nships[rowIndex] < 2:
            rowIndex += 1
            columnIndex == 0
            if rowIndex == 10:
                break
            continue

        if Board.cols_nships[columnIndex] < 1:
            columnIndex += 1
            if columnIndex >= 9:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue
        elif Board.cols_nships[columnIndex+1] < 1:
            columnIndex += 2
            if columnIndex >= 9:
                columnIndex = 0
                rowIndex += 1
                # Não existe mais nenhum ponto
                if rowIndex == 10:
                    break
            continue

        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == LEFT) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+1] != 1:
            
            if (board[rowIndex][columnIndex + 1] == UNKNOWN or
                board[rowIndex][columnIndex + 1] == RIGHT):
                
                grid = [[-1] * 10 for _ in range(10)]
                grid[rowIndex][columnIndex] = LEFT
                grid[rowIndex][columnIndex + 1] = RIGHT

                """
                grid[rowIndex-1][columnIndex-1] = WATER
                grid[rowIndex-1][columnIndex] = WATER
                grid[rowIndex-1][columnIndex+1] = WATER
                grid[rowIndex-1][columnIndex+2] = WATER
                grid[rowIndex][columnIndex-1] = WATER
                grid[rowIndex][columnIndex+2] = WATER
                grid[rowIndex+1][columnIndex-1] = WATER
                grid[rowIndex+1][columnIndex] = WATER
                grid[rowIndex+1][columnIndex+1] = WATER
                grid[rowIndex+1][columnIndex+2] = WATER"""

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
    # existem no total no maximo 90 combinações diferentes de meter esse ship na vertical
    for _ in range(90):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == TOP) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+1][columnIndex] != 1:
            
            if (board[rowIndex + 1][columnIndex] == UNKNOWN or
                board[rowIndex + 1][columnIndex] == BOTTOM):
                
                grid = [[-1] * 10 for _ in range(10)]
                grid[rowIndex][columnIndex] = TOP
                grid[rowIndex + 1][columnIndex] = BOTTOM

                """
                grid[rowIndex-1][columnIndex-1] = WATER
                grid[rowIndex-1][columnIndex] = WATER
                grid[rowIndex-1][columnIndex+1] = WATER
                grid[rowIndex][columnIndex-1] = WATER
                grid[rowIndex][columnIndex+1] = WATER
                grid[rowIndex+1][columnIndex-1] = WATER
                grid[rowIndex+1][columnIndex+1] = WATER
                grid[rowIndex+2][columnIndex-1] = WATER
                grid[rowIndex+2][columnIndex] = WATER
                grid[rowIndex+2][columnIndex+1] = WATER"""

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
    # existem no total no maximo 80 combinações diferentes de meter esse ship na horizontal
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == LEFT) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+1] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+2] != 1:
            
            if (board[rowIndex][columnIndex + 1] == UNKNOWN or
                board[rowIndex][columnIndex + 1] == MIDDLE):
                
                if (board[rowIndex][columnIndex + 2] == UNKNOWN or
                board[rowIndex][columnIndex + 2] == RIGHT):
                    
                    grid = [[-1] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = LEFT
                    grid[rowIndex][columnIndex + 1] = MIDDLE
                    grid[rowIndex][columnIndex + 2] = RIGHT
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
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(80):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == TOP) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+1][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+2][columnIndex] != 1:
            
            if (board[rowIndex + 1][columnIndex] == UNKNOWN or
                board[rowIndex + 1][columnIndex] == MIDDLE):

                if (board[rowIndex + 2][columnIndex] == UNKNOWN or
                    board[rowIndex + 2][columnIndex] == BOTTOM):
                    
                    grid = [[-1] * 10 for _ in range(10)]
                    grid[rowIndex][columnIndex] = TOP
                    grid[rowIndex + 1][columnIndex] = MIDDLE
                    grid[rowIndex + 2][columnIndex] = BOTTOM
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
    # existem no total no maximo 70 combinações diferentes de meter esse ship na horizontal
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == LEFT) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+1] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+2] != 1 and\
            Board.no_ships_matrix[rowIndex][columnIndex+3] != 1:
            
            if (board[rowIndex][columnIndex + 1] == UNKNOWN or
                board[rowIndex][columnIndex + 1] == MIDDLE):

                if (board[rowIndex][columnIndex + 2] == UNKNOWN or
                    board[rowIndex][columnIndex + 2] == MIDDLE):
                    
                    if (board[rowIndex][columnIndex + 3] == UNKNOWN or
                    board[rowIndex][columnIndex + 3] == RIGHT):
                        
                        grid = [[-1] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = LEFT
                        grid[rowIndex][columnIndex + 1] = MIDDLE
                        grid[rowIndex][columnIndex + 2] = MIDDLE
                        grid[rowIndex][columnIndex + 3] = RIGHT
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
    # existem no total no maximo 80 combinações diferentes de meter esse ship na vertical
    for _ in range(70):
        # cria a grid com o barco se for uma posição onde possa haver esse barco
        if (board[rowIndex][columnIndex] == UNKNOWN or
            board[rowIndex][columnIndex] == TOP) and\
            Board.no_ships_matrix[rowIndex][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+1][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+2][columnIndex] != 1 and\
            Board.no_ships_matrix[rowIndex+3][columnIndex] != 1:
            
            if (board[rowIndex + 1][columnIndex] == UNKNOWN or
                board[rowIndex + 1][columnIndex] == MIDDLE):
                
                if (board[rowIndex + 2][columnIndex] == UNKNOWN or
                    board[rowIndex + 2][columnIndex] == MIDDLE):
                    
                    if (board[rowIndex + 3][columnIndex] == UNKNOWN or
                        board[rowIndex + 3][columnIndex] == BOTTOM):
                        
                        grid = [[-1] * 10 for _ in range(10)]
                        grid[rowIndex][columnIndex] = TOP
                        grid[rowIndex + 1][columnIndex] = MIDDLE
                        grid[rowIndex + 2][columnIndex] = MIDDLE
                        grid[rowIndex + 3][columnIndex] = BOTTOM
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
    """Receives a grid with the ships given in the hints and creates all
    possible grids that can be used to solve the puzzle."""
    Board.grids_ship1 = create_grids_ship1(board)
    Board.grids_ship2_hor = create_grids_ship2_horizontal(board)
    Board.grids_ship2_ver = create_grids_ship2_vertical(board)
    Board.grids_ship3_hor = create_grids_ship3_horizontal(board)
    Board.grids_ship3_ver = create_grids_ship3_vertical(board)
    Board.grids_ship4_hor = create_grids_ship4_horizontal(board)
    Board.grids_ship4_ver = create_grids_ship4_vertical(board)


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

    # If (i,j) is 1 cannot be a ship in any grid and 0 otherwise
    # (maybe being a set of numbers that correspond to positions is faster)
    no_ships_matrix = np.array([[-1] * 10 for _ in range(10)])

    def __init__(self, grid):
        self.grid = grid

        # Saves which rows and columns are complete in this Board instance
        self.complete_rows = set()
        self.complete_cols = set()

        # Index 'i' has the number of ships of size i + 1 placed in this Board's grid
        self.nships_of_size = np.zeros(4, np.uint8)

        # Saves additional positions that cannot be a ship in this Board instance
        # Maybe we could just put water in all the spots?
        self.no_ships_pos = set() # 15 = (1,5), 92 = (9,2), etc
    
    def calculate_state(self):
        #TODO
        pass

    def get_int_value(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição da representação do tabuleiro."""
        if 0 <= row <= 9 and 0 <= col <= 9:
            return self.grid[row][col]

    # Não sei se precisa existir, perguntei pra prof
    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        if 0 <= row <= 9 and 0 <= col <= 9:
            match self.grid[row][col]:
                case -1:
                    return "None"
                case 0:
                    return "W"
                case 1:
                    return "L"
                case 2:
                    return "R"
                case 3:
                    return "T"
                case 4:
                    return "B"
                case 5:
                    return "M"
                case 6:
                    return "C"
        else:
            return "None"

    def adjacent_int_vertical_values(self, row: int, col: int) -> (int, int):
        """Devolve os valores inteiros imediatamente acima e abaixo,
        respectivamente."""
        return (self.get_int_value(row-1, col), self.get_int_value(row+1, col))

    # Não sei se precisa existir, perguntei pra prof
    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        return (self.get_value(row - 1, col), self.get_value(row + 1, col))

    def adjacent_int_horizontal_values(self, row: int, col: int) -> (int, int):
        """Devolve os valores inteiros imediatamente acima e abaixo,
        respectivamente."""
        return (self.get_int_value(row, col-1), self.get_int_value(row, col+1))

    # Não sei se precisa existir, perguntei pra prof
    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        return (self.get_value(row, col - 1), self.get_value(row, col + 1))
    
    def can_place_ship(self, row: int, col: int):
        """Returns True if a ship can be placed in the given position"""
        if self.get_int_value(row, col) >= 0:
            return False
        
        adj_horizontal = self.adjacent_int_horizontal_values(row, col)
        adj_vertical = self.adjacent_int_vertical_values(row, col)
        diagonals_left = self.adjacent_int_horizontal_values(row, col - 1) 
        diagonals_right = self.adjacent_int_vertical_values(row, col + 1)

        for n in range(2): # They are all tuples with 2 values each
            if adj_horizontal[n] >= 0 or adj_vertical[n] >= 0 or \
                diagonals_left[n] >= 0 or diagonals_right[n] >= 0:
                return False
        
        return True
    
    def get_row_nships(self, row: int):
        """Returns the number of ships placed in the given row"""
        sum = 0
        if 0 <= row <= 9:
            for col in range(10):
                if self.grid[row][col] >= 0:
                    sum += 1
            return sum
        
    def get_col_nships(self, col: int):
        """Returns the number of ships placed in the given column"""
        sum = 0
        if 0 <= col <= 9:
            for row in range(10):
                if self.grid[row][col] >= 0:
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
            if self.grid[pos[0]][pos[1]] == 0 or self.grid[pos[0]][pos[1]] == -1:
                return False
        
        if self.nships_of_size[0] != 4 or self.nships_of_size[1] == 3 or\
            self.nships_of_size[2] != 2 or self.nships_of_size[3] != 1:
            return False
                
        return True
    
    def get_combined_grid(self, grid): # NOT TESTED
        """Combines the grids if include = True and removes "grid" from the
        combination if include = False"""
        new_grid = [[-1 for _ in range(10)] for _ in range(10)]
        
        for i in range(10):
            for j in range(10):
                if self.grid[i][j] >= 0 and grid[i][j] == -1:
                    new_grid[i][j] = self.grid[i][j]
                elif self.grid[i][j] == -1 and grid[i][j] >= 0:
                    new_grid[i][j] = grid[i][j]
                else:
                    new_grid[i][j] = self.grid[i][j]
        
        return new_grid

    def get_possible_actions(self):
        #TODO
        pass

    def interpret_hints(self, nhints: int):
        """Interprets the given hints and does the following things:
        - Places any ships of size 1 given in the hints in the starting grid
        - Composes the "no_ships" matrix
        - Creates the puzzle's starting grid
        - Checks if any rows or columns have already been completed. If so, adds
        them to the corresponding sets and fills the remaining spots with water"""
        # OBSERVAÇÃO: talvez hints_matrix seja completamente desnecessário,
        # mas talvez não só seja necessário como tenha que ser variável de classe
        hints_matrix = np.array([[-1] * 10 for _ in range(10)])
        starting_grid = [[-1 for _ in range(10)] for _ in range(10)]

        for _ in range(nhints):
            hints_aux = sys.stdin.readline().strip("\n\r")
            hints_aux = hints_aux.split("\t")

            aux = tuple(map(int, hints_aux[1:3]))

            match hints_aux[3]:
                case 'W':
                    hints_matrix[aux[0]][aux[1]] = WATER

                    Board.no_ships_matrix[aux[0]][aux[1]] = 1
                case 'C':
                    hints_matrix[aux[0]][aux[1]] = CENTER
                    Board.hints_pos.append(tuple(map(int, aux)))

                    # If the hint says there is a submarine in this position,
                    # then we can instantly put it in the starting grid.
                    # Put water around it? (needs 'if's so it doesn't go out of bounds )
                    starting_grid[aux[0]][aux[1]] = CENTER
                    Board.no_ships_matrix[aux[0]][aux[1]] = 1
                    self.nships_of_size[0] += 1

                    if (aux[0]-1) != -1:
                        if (aux[1]-1) != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]-1][aux[1]] = 1
                        if (aux[1]+1) != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1

                    if (aux[1]-1) != -1:
                        Board.no_ships_matrix[aux[0]][aux[1]-1] = 1
                    if (aux[1]+1) != 10:
                        Board.no_ships_matrix[aux[0]][aux[1]+1] = 1

                    if (aux[0]+1) != 10:
                        if (aux[1]-1) != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]+1][aux[1]] = 1
                        if (aux[1]+1) != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1
                case 'T':
                    hints_matrix[aux[0]][aux[1]] = TOP
                    Board.hints_pos.append(tuple(map(int, aux)))

                    if aux[0]-1 != -1:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]-1][aux[1]] = 1
                        if aux[1]+1 != 10: 
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1

                    if aux[1]-1 != -1:
                        Board.no_ships_matrix[aux[0]][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        Board.no_ships_matrix[aux[0]][aux[1]+1] = 1

                    if aux[0]+1 != 10:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1
                    if aux[0]+2 != 10:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+2][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+2][aux[1]+1] = 1
                case 'M':
                    hints_matrix[aux[0]][aux[1]] = MIDDLE
                    Board.hints_pos.append(tuple(map(int, aux)))

                    if aux[0]-1 != -1:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1

                    if aux[0]+1 != 10:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1
                case 'B':
                    hints_matrix[aux[0]][aux[1]] = BOTTOM
                    Board.hints_pos.append(tuple(map(int, aux)))

                    if aux[0]-2 != -1:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-2][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]-2][aux[1]+1] = 1

                    if aux[0]-1 != -1:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1

                    if aux[1]-1 != -1:
                        Board.no_ships_matrix[aux[0]][aux[1]-1] = 1
                    if aux[1]+1 != 10:
                        Board.no_ships_matrix[aux[0]][aux[1]+1] = 1

                    if aux[0]+1 != 10:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]+1][aux[1]] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1
                case 'L':
                    hints_matrix[aux[0]][aux[1]] = LEFT
                    Board.hints_pos.append(tuple(map(int, aux)))

                    if aux[0]-1 != -1:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]-1][aux[1]] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1
                        if aux[1]+2 != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+2] = 1

                    if aux[1]-1 != -1:
                        Board.no_ships_matrix[aux[0]][aux[1]-1] = 1

                    if aux[0]+1 != 10:
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]+1][aux[1]] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1
                        if aux[1]+2 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+2] = 1
                case 'R':
                    hints_matrix[aux[0]][aux[1]] = RIGHT
                    Board.hints_pos.append(tuple(map(int, aux)))

                    if aux[0]-1 != -1:
                        if aux[1]-2 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-2] = 1
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]-1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]-1][aux[1]] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]-1][aux[1]+1] = 1

                    if aux[1]+1 != 10:
                        Board.no_ships_matrix[aux[0]][aux[1]+1] = 1

                    if aux[0]+1 != 10:
                        if aux[1]-2 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-2] = 1
                        if aux[1]-1 != -1:
                            Board.no_ships_matrix[aux[0]+1][aux[1]-1] = 1
                        Board.no_ships_matrix[aux[0]+1][aux[1]] = 1
                        if aux[1]+1 != 10:
                            Board.no_ships_matrix[aux[0]+1][aux[1]+1] = 1

        self.grid = starting_grid
        
        for n in range(10):
            self.check_close_col(n)
            self.check_close_row(n)
        
        create_grids(hints_matrix)

        self.grid = starting_grid

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """
        # TODO

        from sys import stdin
        rows_nships = stdin.readline().strip("\n")
        rows_nships = rows_nships.split("\t")
        rows_nships = rows_nships[1:]
        Board.rows_nships = (tuple(map(int, rows_nships)))
        # print("Ships per row: \n", Board.rows_nships)

        cols_nships = stdin.readline().strip("\n")
        cols_nships = cols_nships.split("\t")
        cols_nships = cols_nships[1:]
        Board.cols_nships = (tuple(map(int, cols_nships)))
        # print("Ships per columnn: \n", Board.cols_nships)

        nhints = int(input())

        starting_board = Board([])
        starting_board.interpret_hints(nhints)

        #print("Starting grid:\n", np.array(starting_board.grid))

        #print("Number of size 4 horizontal ships: ", len(Board.grids_ship4_hor))
        #print("Grid 10 of size 4 horizontal:\n", np.array(Board.grids_ship4_hor[10]))

        #print("Combined grid of starting grid and the previous grid:\n", np.array(starting_board.get_combined_grid(Board.grids_ship4_hor[10])))

        # print("Number of ships placed of each size:\n", starting_board.nships_of_size)

        # print("Positions of the hints:\n", Board.hints_pos)
        # print("Positions that cannot have ships\n", Board.no_ships_matrix)

        return Board(starting_board)

    def __str__(self): #TODO
        """When printing a class, this function gets called.
        Make it print the grid's representation, please"""
        pass


class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        state = BimaruState(board)
        super().__init__(state)
        pass

    def actions(self, state: BimaruState): #INCORRECT!
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        actions = []

        # TODO
        
        return actions

    def result(self, state: BimaruState, action): # INCORRECT!
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        
        new_grid = state.board.get_combined_grid(action[1])
        new_state = BimaruState(new_grid)

        return new_state
        pass

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        return state.board.check_objective()

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board = Board.parse_instance()
    bimaru = Bimaru(board)

    pass
