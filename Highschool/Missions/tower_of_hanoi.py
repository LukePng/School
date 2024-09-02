class Tower:
    def __init__(self, ):
        self.disks = []
    def push_disk(self, disk):
        self.disks.append(disk)
    def pop_disk(self):
        return self.disks.pop()
    def peek_top_disk(self):
        if self.disks:
            return self.disks[-1]
        return -1
    def __str__(self):
        return str(self.disks)

        

class TowerOfHanoi:
    def __init__(self, n):
        self.towers = {'A': Tower(), 'B':Tower(), 'C':Tower()}
        self.n = n
        self.step = 0
    def get_Tower(self, tower):
        return self.towers[tower]
    def get_n(self):
        return self.n
    def reset_step(self):
        self.step = 0
    def get_step(self):
        return self.step
    def reset_towers(self):
        self.towers['C'] = Tower()
        self.towers['B'] = Tower()
        self.towers['A'] = Tower()
        for i in range(self.n):
            self.towers['A'].push_disk(self.n-i)
    def print_towers(self):
        print('A: {}\nB: {}\nC: {}'.format(self.towers['A'], self.towers['B'], self.towers['C']))

    def check_win(self):
        win_pattern = [i for i in range(1, self.n+1)]
        pattern = []
        while self.towers['C'].peek_top_disk() != -1:
            pattern.append(self.towers['C'].pop_disk())
        print(win_pattern)
        print(pattern)
        print(win_pattern == pattern)
        if win_pattern == pattern:
            print('You win!\nTotal steps taken: {},\nOptimal steps expected: {}'.format(self.step, 2**self.n-1))
            return True
        else:
            pattern = pattern[::-1]
            for i in pattern:
                self.towers['C'].push_disk(i)
        return False
    
    def move_disk(self, src, dst):
        if self.towers[src].peek_top_disk() == -1:
            print('Error, source tower is empty!')
            return
        if (self.towers[dst].peek_top_disk() > self.towers[src].peek_top_disk()) or (self.towers[dst].peek_top_disk() == -1):
            self.towers[dst].push_disk(self.towers[src].pop_disk())
            self.step += 1

    def solve(self):
        self.reset_towers()
        self.reset_step()
        def recur_sol(n, src, dst, aux,):
            if n == 0:
                return
            recur_sol(n-1, src, aux, dst)
            self.towers[dst].push_disk(self.towers[src].pop_disk())
            self.step += 1
            print('Step {}:\nA: {}\nB: {}\nC: {}'.format(self.step, self.towers['A'], self.towers['B'], self.towers['C']))
            recur_sol (n-1, aux, dst, src)
        recur_sol(self.n, 'A', 'C', 'B')

new_game = TowerOfHanoi(3)
new_game.reset_towers()
def program():
    while True:
        print('Please choose one of the following options:\n1. Start/Reset a new game\n2. Move a disk\n3. Auto-solve game\n4. Quit')
        print('Steps: {}'.format(new_game.get_step()))
        new_game.print_towers()
        choice = input('Your choice: ')
        if choice == '1':
            new_game.reset_towers()
            new_game.reset_step()
            print('New game started!')
            new_game.print_towers()
        elif choice == '2':
            src = input('Please enter the source tower: ')
            dst = input('Please enter the destination tower: ')
            new_game.move_disk(src, dst)
            new_game.print_towers()
            if new_game.check_win():
                break
        elif choice == '3':
            print('Auto-solving game...')
            new_game.solve()
            if new_game.check_win():
                break

        elif choice == '4':
            print('Goodbye!')
            break
program()