
"""
retorna um vector de matrizes com todas as formas de meter um barco

tamanho do vector: 580
                        +---   indice   ---+
os barcos de tamanho 1: 0 - 99               -> total 100
os barcos de tamanho 2: 100 - 189, 190 - 279 -> total 180 (90 na vertical e horizontal)
os barcos de tamanho 3: 280 - 359, 360 - 439 -> total 160 (80 na vertical e horizontal)
os barcos de tamanho 4: 440 - 509, 510 - 579 -> total 140 (70 na vertical e horizontal)
"""


def create_grids_ship1():
    """ inicializa tudo a water """
    grids = [[["." for _ in range(10)] for _ in range(10)] for _ in range(100)]

    """ poem circle em todas posições onde pode estar na grid """
    for gridNumber in range(100):
        i = gridNumber // 10
        j = gridNumber % 10
        grids[gridNumber][i][j] = "C"

    return grids

def create_grids_ship2():
    """ inicializa tudo a water """
    grids = [[["." for _ in range(10)] for _ in range(10)] for _ in range(180)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(9):
            grids[gridNumber][i][j] = "L"
            grids[gridNumber][i][j+1] = "R"
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(9):
        for j in range(10):
            grids[gridNumber][i][j] = "T"
            grids[gridNumber][i+1][j] = "B"
            gridNumber += 1

    return grids

def create_grids_ship3():
    """ inicializa tudo a water """
    grids = [[["." for _ in range(10)] for _ in range(10)] for _ in range(160)]
    gridNumber = 0

    """ poem o barco na horizontal """
    for i in range(10):
        for j in range(8):
            grids[gridNumber][i][j] = "L"
            grids[gridNumber][i][j+1] = "M"
            grids[gridNumber][i][j+2] = "R"
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(8):
        for j in range(10):
            grids[gridNumber][i][j] = "T"
            grids[gridNumber][i+1][j] = "M"
            grids[gridNumber][i+2][j] = "B"
            gridNumber += 1

    return grids

def create_grids_ship4():
    """ inicializa tudo a water """
    grids = [[["." for _ in range(10)] for _ in range(10)] for _ in range(140)]
    gridNumber = 0

    for i in range(10):
        for j in range(7):
            grids[gridNumber][i][j] = "L"
            grids[gridNumber][i][j+1] = "M"
            grids[gridNumber][i][j+2] = "M"
            grids[gridNumber][i][j+3] = "R"
            gridNumber += 1

    """ poem o barco na vertical """
    for i in range(7):
        for j in range(10):
            grids[gridNumber][i][j] = "T"
            grids[gridNumber][i+1][j] = "M"
            grids[gridNumber][i+2][j] = "M"
            grids[gridNumber][i+3][j] = "B"
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

print_all_grids(create_grids())