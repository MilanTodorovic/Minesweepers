import random
GRID_SIZE = 20
MINES = 20
ALIVE = True

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
    global GRID_SIZE, number_grid

    if ( x >= 0 and x <= GRID_SIZE-1) and (y >= 0 and y <= GRID_SIZE-1):
        if number_grid[x][y]:  # and n_grid[x][y] != -1:
            return (x,y)
        else:
            reveal_neighbours(x+1, y)
            reveal_neighbours(x-1, y)
            reveal_neighbours(x, y+1)
            reveal_neighbours(x, y-1)
            return (x,y)
    else:
        pass
    
def check_for_mines(x, y, m_grid, n_grid, u_grid):
    global ALIVE
    queue = []
    if m_grid[x][y]:
        print("You died.")
        ALIVE = False
    else:
        queue = reveal_neighbours(x, y)
        for q in queue:
            if q:
                x, y = q
                u_grid[x][y] = str(n_grid[x][y])

# PREPARATIONS            
mine_grid = []
number_grid = []
user_grid = []

populate_user_grid(user_grid)
place_mines(mine_grid)
pre_populate_number_grid(number_grid)
place_numbers(mine_grid, number_grid)

for i in range(GRID_SIZE):
    print(mine_grid[i])
print()
for i in range(GRID_SIZE):
    print(number_grid[i])
    
# THE GAME LOOP
while ALIVE:
    print()
    print("\n".join(" ".join(i for i in item) for item in user_grid))
    print("Enter two numbers between 0 and 19: ")
    x,y = map(int, input().split())
    check_for_mines(x, y, mine_grid, number_grid, user_grid)
