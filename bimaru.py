# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 115:
# 103811 Tiago Deane
# 104145 Artur Krystopchuk

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
                Board.M[aux[0]][aux[1]] = 0

                Board.no_ships.append(aux)
            case 'C':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1])))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0], aux[1]-1)))
                Board.no_ships.append(tuple((aux[0], aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1])))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))
            case 'T':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1])))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0], aux[1]-1)))
                Board.no_ships.append(tuple((aux[0], aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+2, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+2, aux[1]+1)))
            case 'M':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))
            case 'B':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-2, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-2, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0], aux[1]-1)))
                Board.no_ships.append(tuple((aux[0], aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1])))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))
            case 'L':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1])))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+2)))
                Board.no_ships.append(tuple((aux[0], aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1])))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+2)))
            case 'R':
                Board.M[aux[0]][aux[1]] = 1
                Board.hints_pos.append(tuple(map(int, aux)))

                Board.no_ships.append(tuple((aux[0]-1, aux[1]-2)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]-1, aux[1])))
                Board.no_ships.append(tuple((aux[0]-1, aux[1]+1)))
                Board.no_ships.append(tuple((aux[0], aux[1]+1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-2)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]-1)))
                Board.no_ships.append(tuple((aux[0]+1, aux[1])))
                Board.no_ships.append(tuple((aux[0]+1, aux[1]+1)))

    Board.M = tuple(tuple(row) for row in Board.M)

def create_grids_ship1():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(100)]

    """ poem circle em todas posições onde pode estar na grid """
    for gridNumber in range(100):
        i = gridNumber // 10
        j = gridNumber % 10

        if (i,j) in Board.no_ships:
            continue

        grids[gridNumber][i][j] = 1

        grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
        Board.all_grids.append(tuple(grids[gridNumber]))

    return grids

def create_grids_ship2():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(180)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(9):
            if (i,j) in Board.no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            
            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(9):
        for j in range(10):
            if (i,j) in Board.no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids_ship3():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(160)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(8):
            if (i,j) in Board.no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            grids[gridNumber][i][j+2] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(8):
        for j in range(10):
            if (i,j) in Board.no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1
            grids[gridNumber][i+2][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids_ship4():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(140)]
    gridNumber = 0

    for i in range(10):
        for j in range(7):
            if (i,j) in Board.no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            grids[gridNumber][i][j+2] = 1
            grids[gridNumber][i][j+3] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(grids[gridNumber])
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(7):
        for j in range(10):
            if (i,j) in Board.no_ships:
                continue
            
            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1
            grids[gridNumber][i+2][j] = 1
            grids[gridNumber][i+3][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            Board.all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids():
    create_grids_ship1() + create_grids_ship2() + create_grids_ship3() + create_grids_ship4()


class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1
        self.included = [0 for _ in range(len(Board.all_grids))]

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de Bimaru."""

    rows_nships = []
    cols_nships = []

    all_grids = []
    no_ships = []
    hints_pos = []

    # Not sure if this last one is gonna be used
    M = np.array(np.array([[100] * 10 for _ in range(10)]))

    def __init__(self, grid):
        self.grid = grid

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        if 0 <= row <= 9 and 0 <= col <= 9:
            return self.grid[row][col]

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        return (self.get_value(row - 1, col), self.get_value(row + 1, col))

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        return (self.get_value(row, col - 1), self.get_value(row, col + 1))
    
    def update_grid(self, grid, include=True):
        """Combines the grids if include = True and removes "grid" from the
        combination if include = False"""
        new_grid = [[0 for _ in range(10)] for _ in range(10)]
        
        if include:
            for i in range(10):
                for j in range(10):
                    if self.grid[i][j] == 1 and grid[i][j] == 1:
                        new_grid[i][j] = 1
                        continue
                    new_grid[i][j] = self.grid[i][j] + grid[i][j]
        else:
            for i in range(10):
                for j in range(10):
                    if self.grid[i][j] == 0 and grid[i][j] == 0:
                        new_grid[i][j] = 0
                        continue
                    new_grid[i][j] = self.grid[i][j] - grid[i][j]
        return new_grid


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

        cols_nships = stdin.readline().strip("\n")
        cols_nships = cols_nships.split("\t")
        cols_nships = cols_nships[1:]
        Board.cols_nships = (tuple(map(int, cols_nships)))

        nhints = int(input())

        # Builds the 'no_ship' and 'hints_pos' lists
        interpret_hints(nhints)

        starting_grid = [[0 for _ in range(10)] for _ in range(10)]

        return Board(starting_grid)

        # RETURNS A BOARD
        pass


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
        actions = []

        # Each action is a tuple of 3 elements: either "include" or "exclude",
        # followed by a grid, followed by the grid's index in all_grids
        for i in range(len(state.board.all_grids)):
            if state.included[i] == 0:
                actions.append(("include", Board.all_grids[i], i))
            elif state.included[i] == 1:
                actions.append(("exclude", Board.all_grids[i], i))
        
        return actions

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        if action[0] == "include":
            new_grid = state.board.update_grid(action[1])
            new_state = BimaruState(new_grid)
            new_state.included[action[2]] = 1
        else:
            new_grid = state.board.update_grid(action[1], include=False)
            new_state = BimaruState(new_grid)
            new_state.included[action[2]] = 0

        return new_state
        """Esta função retorna o state resultante da ação. Temos que criar mais
        um Board e um State e devolver isso (pra poderem voltar pra trás)? E
        nesse caso, 'update_grid' tem que devolver a nova grid resultante da
        ação ao invés de alterar a grid do Board..."""
        pass

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

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

    pass
