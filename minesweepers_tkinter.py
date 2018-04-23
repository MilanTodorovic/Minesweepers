import random, platform
import tkinter as tk


class Game(tk.Tk):

    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.master = master
        self.GRID_SIZE = 20
        self.MINES = self.GRID_SIZE
        self.ALIVE = True
        self.COLORED_TEXT = platform.release() == "10"
        self.RED   = "\033[1;31m"
        self.BLUE  = "\033[1;34m"
        self.CYAN  = "\033[1;36m"
        self.GREEN = "\033[0;32m"
        self.RESET = "\033[0;0m"
        self.BOLD  = "\033[;1m"
        self.REVERSE = "\033[;7m"
        # PREPARATIONS
        self.MINE_GRID = []
        self.NUMBER_GRID = []
        self.USER_GRID = []
        self.REVEALED = set()
        self.UNOPENED_FIELDS = self.GRID_SIZE*self.GRID_SIZE  # not a constant

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH)
        self.strVars = [tk.StringVar() for i in range(self.GRID_SIZE*self.GRID_SIZE)]
        self.buttons = [tk.Button(self.frame, text="?", textvariable=self.strVars[i], command=lambda i=i: self.check_for_mines(i))
                            for i in range(self.GRID_SIZE*self.GRID_SIZE)]
        for btn in self.buttons:
            btn.pack()
        
        self.populate_user_grid()
        self.place_mines()
        self.pre_populate_number_grid()
        self.place_numbers()

##        for i in range(self.GRID_SIZE):
##            print(self.MINE_GRID[i])
##        print()
##        for i in range(self.GRID_SIZE):
##            print(self.NUMBER_GRID[i])
##        self.game_loop()

    def game_loop(self):
        # THE GAME LOOP
        while self.ALIVE and self.MINES != self.UNOPENED_FIELDS:
            print()
            print("\n".join(" ".join(i for i in item) for item in self.USER_GRID))
            print("Enter two numbers between 0 and {} (fields remaining {}): ".format(self.GRID_SIZE-1, self.UNOPENED_FIELDS))
            x,y = map(int, input().split())
            self.check_for_mines(x, y)
            self.UNOPENED_FIELDS = len([i for u in self.USER_GRID for i in u if i == "?"])

    def populate_user_grid(self):
        for i in range(self.GRID_SIZE):
            self.USER_GRID.append(["?" for j in range(self.GRID_SIZE)])

    def pre_populate_number_grid(self):
        for i in range(self.GRID_SIZE):
            self.NUMBER_GRID.append([0 for j in range(self.GRID_SIZE)])

    def place_mines(self):
        s = set()
        while len(s) < self.MINES:
            s.add((random.randint(0,self.GRID_SIZE-1),random.randint(0,self.GRID_SIZE-1)))
        for i in range(self.GRID_SIZE):
            self.MINE_GRID.append([0 for j in range(self.GRID_SIZE)])
        for j in s:
            x, y = j
            print(x,y)
            self.MINE_GRID[x][y] = 1
        

    def place_numbers(self):
        self.sorounding_mines = 0
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                # print("i = {} j ={}".format(i,j))
                if not i:  # i = 0
                    if not j:  # j = 0
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j+1]:
                            self.sorounding_mines += 1
                    elif j == self.GRID_SIZE-1:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j-1]:
                            self.sorounding_mines += 1
                    else:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j-1]:
                            self.sorounding_mines += 1
                    self.NUMBER_GRID[i][j] = self.sorounding_mines
                    self.sorounding_mines = 0
                elif i == self.GRID_SIZE-1:
                    if not j:  # j = 0
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j+1]:
                            self.sorounding_mines += 1
                    elif j == self.GRID_SIZE-1:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j-1]:
                            self.sorounding_mines += 1
                    else:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j-1]:
                            self.sorounding_mines += 1
                    self.NUMBER_GRID[i][j] = self.sorounding_mines
                    self.sorounding_mines = 0
                else:
                    if not j:  # j = 0
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j+1]:
                            self.sorounding_mines += 1
                    elif j == self.GRID_SIZE-1:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j-1]:
                            self.sorounding_mines += 1
                    else:
                        if self.MINE_GRID[i][j]:
                            self.NUMBER_GRID[i][j] = -1
                            continue
                        if self.MINE_GRID[i][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i+1][j-1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j+1]:
                            self.sorounding_mines += 1
                        if self.MINE_GRID[i-1][j-1]:
                            self.sorounding_mines += 1
                    self.NUMBER_GRID[i][j] = self.sorounding_mines
                    self.sorounding_mines = 0

    def reveal_neighbours(self, x, y):
        if ( x >= 0 and x <= self.GRID_SIZE-1) and (y >= 0 and y <= self.GRID_SIZE-1):
            if (x,y) in self.REVEALED:
                # print("Revealed pair found {} {}".format(x,y))
                pass
            else:
                if self.NUMBER_GRID[x][y]:  # and n_grid[x][y] != -1:
                    self.REVEALED.add((x, y))
                else:
                    self.REVEALED.add((x, y))
                    self.reveal_neighbours(x+1, y)
                    self.reveal_neighbours(x-1, y)
                    self.reveal_neighbours(x, y+1)
                    self.reveal_neighbours(x, y-1)

    def check_for_mines(self, x):
        x = x//self.GRID_SIZE
        y = x%self.GRID_SIZE
        print(x,y)
        if self.MINE_GRID[x][y]:
            print("You died.")
            self.ALIVE = False
            for i in range(self.GRID_SIZE):
                for j in range(self.GRID_SIZE):
                    if self.MINE_GRID[i][j]:
                        if self.COLORED_TEXT:
                            self.USER_GRID[i][j] = self.RED + "M" + self.RESET
                        else:
                            self.USER_GRID[i][j] = "M"
            print("\n".join(" ".join(i for i in item) for item in self.USER_GRID))
        else:
            self.reveal_neighbours(x, y)
            for coord in self.REVEALED:
                x, y = coord
                if self.COLORED_TEXT:
                    self.USER_GRID[x][y] = self.GREEN + str(self.NUMBER_GRID[x][y]) + self.RESET if self.NUMBER_GRID[x][y] > 0 else self.BLUE + str(self.n_grid[x][y]) + self.RESET
                else:
                    self.USER_GRID[x][y] = str(self.NUMBER_GRID[x][y])


if __name__ == "__main__":
    game = Game()
    game.mainloop()
