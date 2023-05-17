
"""
retorna um vector de matrizes com todas as formas de meter um barco

tamanho do vector: 580
                        +---   indice   ---+
os barcos de tamanho 1: 0 - 99               -> total 100
os barcos de tamanho 2: 100 - 189, 190 - 279 -> total 180 (90 na vertical e horizontal)
os barcos de tamanho 3: 280 - 359, 360 - 439 -> total 160 (80 na vertical e horizontal)
os barcos de tamanho 4: 440 - 509, 510 - 579 -> total 140 (70 na vertical e horizontal)
"""

import numpy as np

all_grids = []
no_ships = [(0, 0)]

def create_grids_ship1():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(100)]

    """ poem circle em todas posições onde pode estar na grid """
    for gridNumber in range(100):
        i = gridNumber // 10
        j = gridNumber % 10

        if (i,j) in no_ships:
            continue

        grids[gridNumber][i][j] = 1

        grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
        all_grids.append(tuple(grids[gridNumber]))

    return grids

def create_grids_ship2():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(180)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(9):
            if (i,j) in no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            
            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(9):
        for j in range(10):
            if (i,j) in no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids_ship3():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(160)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(8):
            if (i,j) in no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            grids[gridNumber][i][j+2] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(8):
        for j in range(10):
            if (i,j) in no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1
            grids[gridNumber][i+2][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids_ship4():
    """ inicializa tudo a water """
    grids = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(140)]
    gridNumber = 0

    for i in range(10):
        for j in range(7):
            if (i,j) in no_ships:
                continue

            grids[gridNumber][i][j] = 1
            grids[gridNumber][i][j+1] = 1
            grids[gridNumber][i][j+2] = 1
            grids[gridNumber][i][j+3] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(grids[gridNumber])
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(7):
        for j in range(10):
            if (i,j) in no_ships:
                continue
            
            grids[gridNumber][i][j] = 1
            grids[gridNumber][i+1][j] = 1
            grids[gridNumber][i+2][j] = 1
            grids[gridNumber][i+3][j] = 1

            grids[gridNumber] = tuple(tuple(line) for line in grids[gridNumber])
            all_grids.append(tuple(grids[gridNumber]))
            gridNumber += 1

    return grids

def create_grids():
    return create_grids_ship1() + create_grids_ship2() + create_grids_ship3() + create_grids_ship4()
                
def print_all_grids(grids):
    gridNum = 0
    for i in range(len(grids)):
        print_grid(grids[i])
        print("grid numero:", gridNum)
        gridNum += 1

def print_grid(grid):
    for i in range(10):
        for j in range(10):
            print(grid[i][j], end="")
        """ enter """
        print("")

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
        self.actions(state)."""
        if action[0] == "include":
            update_solution_grid(solution_grid, action[1])
            included[action[2]] = 1
        else:
            update_solution_grid(solution_grid, action[1], include=False)
            included[action[2]] = 0

        return solution_grid

def update_solution_grid(solution_grid, grid, include=True):
    # Overlay the cells of the grid onto the solution grid
    if include:
        for i in range(10):
            for j in range(10):
                if solution_grid[i][j] == 1 and grid[i][j] == 1:
                    continue
                solution_grid[i][j] += grid[i][j]
    else:
        for i in range(10):
            for j in range(10):
                if solution_grid[i][j] == 0 and grid[i][j] == 0:
                    continue
                solution_grid[i][j] -= grid[i][j]
    return solution_grid

create_grids()
solution_grid = np.zeros((10,10), dtype=np.int8)
included = [0 for _ in range(len(all_grids))]

print(len(all_grids))

print("\nSolution grid (empty): \n", solution_grid)
update_solution_grid(solution_grid, all_grids[103])
included[103] = 1
print("\nSolution grid after including grid 103: \n", solution_grid)
update_solution_grid(solution_grid, all_grids[125])
included[125] = 1
print("\nSolution grid after including grid 125: \n", solution_grid)
update_solution_grid(solution_grid, all_grids[103], include=False)
included[103] = 0
print("\nSolution grid after excluding grid 103: \n", solution_grid)

action_list = actions()
print("\nNumber of actions: ", len(action_list))
print("\nAction 103: \n", action_list[103])
print("\nAction 125: \n", action_list[125])

result(solution_grid, action_list[125])
action_list = actions() # needs to calculate "actions" again after every "result"

print("\nSolution grid after applying \"result\" with action 125 (removed it): \n", solution_grid)
print("\nAction 125 after applying \"result\" (now it's include again): \n", action_list[125])
