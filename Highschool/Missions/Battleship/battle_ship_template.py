import random


def get_mapping():
    f = open("ship_class_mapping.txt", "r")
    data = f.read().split("\n")[1:]
    f.close()

    data = list(map(lambda row: row.split(", "), data))
    ship_class_mapping = dict(
        map(lambda row: (row[0], (row[1], int(row[2]))), data))
    return ship_class_mapping


ship_class_mapping = get_mapping()
print(get_mapping())
# ship_class_mapping = {'Carrier': ('C', 5),
# 'Battleship': ('B', 4),
# 'Heavy Cruiser': ('H', 3),
# 'Light Cruiser': ('L', 3),
# 'Submarine': ('S', 3),
# 'Destroyer': ('D', 2),
# 'Torpedo Boat': ('T', 2)}

# your code here
class Ship:
    def __init__(self, cls):
        self._class = cls

    def get_class(self):
        return self._class
    
    def get_abbr(self):
        return ship_class_mapping[self._class][0]
    
    def get_size(self):
        return ship_class_mapping[self._class][1]

class Board:
    def __init__(self):
        self.size = 10
        self._ship_coords = []
        self._board = [['-' for i in range(self.size)] for j in range(self.size)]
        self._guess_board = [['-' for i in range(self.size)] for j in range(self.size)]

    def add_ship(self, ship):
        direction = random.randint(0, 1)
        if direction == 0: # horizontal
            possible = False
            while not possible:
                start_row = random.randint(0, self.size - ship.get_size())
                col = random.randint(0, self.size - 1)
                for i in range(ship.get_size()):
                    if self._board[start_row + i][col] == '-':
                        possible = True
                    else:
                        possible = False
                        break
                if possible:
                    temp = []
                    abbr = ship.get_abbr()
                    for i in range(ship.get_size()):
                        self._board[start_row + i][col] = abbr
                        temp.append([abbr, start_row + i, col])
                    self._ship_coords.append(temp)
    


        elif direction == 1: # vertical
            possible = False
            while not possible:
                start_col = random.randint(0, self.size - ship.get_size())
                row = random.randint(0, self.size - 1)
                for i in range(ship.get_size()):
                    if self._board[row][start_col + i] == '-':
                        possible = True
                    else:
                        possible = False
                        break

                if possible:
                    temp = []
                    abbr = ship.get_abbr()
                    for i in range(ship.get_size()):
                        self._board[row][start_col + i] = abbr
                        temp.append([abbr, row, start_col + i])
                    self._ship_coords.append(temp)
    

    def display_board(self, guess_mode):
        if guess_mode == True:
            return self._guess_board
        else:
            return self._board
    
    def generate_new_game(self):
        ships=[Ship(i) for i in ship_class_mapping.keys()]
        self._ship_coords = []
        self._board = [['-' for i in range(self.size)] for j in range(self.size)]
        self._guess_board = [['-' for i in range(self.size)] for j in range(self.size)]

        for s in ships:
            for i in range(random.randint(1,3)):
                self.add_ship(s)

    def guess(self, row, col):
        if self._guess_board[row][col] == 'X':
            print('Already guessed!\n')
            return False
        else:
            if self._board[row][col] == '-':
                self._guess_board[row][col] = 'X'
                print('Miss!\n')
                return True
            else:
                self._guess_board[row][col] = self._board[row][col]
                print('Hit!\n')
                return True
        
    def power_guess(self, row, col):
        if self._guess_board[row][col] == 'X':
            print('Already guessed!\n')
            return False
        else:
            if self._board[row][col] == '-':
                print(self._guess_board[row][col] == 'X')
                self._guess_board[row][col] = 'X'
                print('Miss!\n')
                return True
            else:
                abbr = self._board[row][col]
                temp = [abbr, row, col]
                for i in self._ship_coords:
                    if temp in i:
                        print(i)
                        for j in i:
                            self._guess_board[j[1]][j[2]] = j[0]
                        print('Hit!\n')
                        return True


    def check_win(self):
        temp = self._guess_board
        for i in range(self.size):
            for j in range(self.size):
                if temp[i][j] == 'X':
                    temp[i][j] = '-'
                if temp[i][j] == '-' and self._board[i][j] != '-':
                    return False
        return True


board = Board()
board.generate_new_game()

while True:
    print("Welcome to Battleship!")
    print("Choose and option from below:")
    print("1) Normal Guess \n2) Power Guess \n3) Show Answer \n4) Restart Game \n5) Exit")
    print("Current Board:")
    print(board.display_board(True))
    print('')
    choice = input("Enter your choice: ")

    if choice == '1':
        row = int(input("Enter row: "))-1
        col = int(input("Enter col: "))-1
        board.guess(row, col)
        

    elif choice == '2':
        row = int(input("Enter row: "))-1
        col = int(input("Enter col: "))-1
        board.power_guess(row, col)

        if board.check_win():
            print('You win!')
            print('Generating new game...')
            board.generate_new_game()

    elif choice == '3':
        print(board.display_board(False))

    elif choice == '4':
        board.generate_new_game()
        print(board.display_board(True))
        print('New game generated')

    elif choice == '5':
        break

    else:
        print("Invalid choice. Try again.")
