import random
GRID_SIZE = 20
MINES = GRID_SIZE
ALIVE = True
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"
REVERSE = "\033[;7m"
# PREPARATIONS
MINE_GRID = []
NUMBER_GRID = []
USER_GRID = []
REVEALED = set()
UNOPENED_FIELDS = GRID_SIZE*GRID_SIZE  # not a constant

def populate_user_grid(grid):
    global GRID_SIZE
    for i in range(GRID_SIZE):
        grid.append(["?" for j in range(GRID_SIZE)])

def pre_populate_number_grid(grid):
    global GRID_SIZE
    for i in range(GRID_SIZE):
        grid.append([0 for j in range(GRID_SIZE)])

def place_mines(grid):
    global GRID_SIZE
    global MINES
    s = set()
    while len(s) < MINES:
        s.add((random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)))
    for i in range(GRID_SIZE):
        grid.append([0 for j in range(GRID_SIZE)])
    for j in s:
        x, y = j
        print(x,x)
        grid[x][y] = 1
        

def place_numbers(mine_grid, grid):
    global GRID_SIZE
    sorounding_mines = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # print("i = {} j ={}".format(i,j))
            if not i:  # i = 0
                if not j:  # j = 0
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j+1]:
                        sorounding_mines += 1
                elif j == GRID_SIZE-1:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j-1]:
                        sorounding_mines += 1
                else:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j-1]:
                        sorounding_mines += 1
                grid[i][j] = sorounding_mines
                sorounding_mines = 0
            elif i == GRID_SIZE-1:
                if not j:  # j = 0
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j+1]:
                        sorounding_mines += 1
                elif j == GRID_SIZE-1:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j-1]:
                        sorounding_mines += 1
                else:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j-1]:
                        sorounding_mines += 1
                grid[i][j] = sorounding_mines
                sorounding_mines = 0
            else:
                if not j:  # j = 0
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j+1]:
                        sorounding_mines += 1
                elif j == GRID_SIZE-1:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j-1]:
                        sorounding_mines += 1
                else:
                    if mine_grid[i][j]:
                        grid[i][j] = -1
                        continue
                    if mine_grid[i][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i+1][j-1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j+1]:
                        sorounding_mines += 1
                    if mine_grid[i-1][j-1]:
                        sorounding_mines += 1
                grid[i][j] = sorounding_mines
                sorounding_mines = 0

def reveal_neighbours(x, y):
    global GRID_SIZE, NUMBER_GRID, REVEALED

    if ( x >= 0 and x <= GRID_SIZE-1) and (y >= 0 and y <= GRID_SIZE-1):
        if (x,y) in REVEALED:
            # print("Revealed pair found {} {}".format(x,y))
            pass
        else:
            if NUMBER_GRID[x][y]:  # and n_grid[x][y] != -1:
                REVEALED.add((x, y))
            else:
                REVEALED.add((x, y))
                reveal_neighbours(x+1, y)
                reveal_neighbours(x-1, y)
                reveal_neighbours(x, y+1)
                reveal_neighbours(x, y-1)

def check_for_mines(x, y, m_grid, n_grid, u_grid):
    global ALIVE, REVEALED, GREEN, RESET, RED
    if m_grid[x][y]:
        print("You died.")
        ALIVE = False
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if m_grid[i][j]:
                    u_grid[i][j] = RED + "M" + RESET
        print("\n".join(" ".join(i for i in item) for item in USER_GRID))
    else:
        reveal_neighbours(x, y)
        for coord in REVEALED:
            x, y = coord
            u_grid[x][y] = GREEN + str(n_grid[x][y]) + RESET if n_grid[x][y] > 0 else BLUE + str(n_grid[x][y]) + RESET

populate_user_grid(USER_GRID)
place_mines(MINE_GRID)
pre_populate_number_grid(NUMBER_GRID)
place_numbers(MINE_GRID, NUMBER_GRID)

for i in range(GRID_SIZE):
    print(MINE_GRID[i])
print()
for i in range(GRID_SIZE):
    print(NUMBER_GRID[i])
    
# THE GAME LOOP
while ALIVE and MINES != UNOPENED_FIELDS:
    print()
    print("\n".join(" ".join(i for i in item) for item in USER_GRID))
    print("Enter two numbers between 0 and {} (fields remaining {}): ".format(GRID_SIZE-1, UNOPENED_FIELDS))
    x,y = map(int, input().split())
    check_for_mines(x, y, MINE_GRID, NUMBER_GRID, USER_GRID)
    UNOPENED_FIELDS = len([i for u in USER_GRID for i in u if i == "?"])
