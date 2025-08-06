class Grid:
    def __init__(self):
        self.positions = {i: "" for i in range(1,10)}
        self.finished = False
    def mark(self, pos, obj):
        self.positions[pos] = obj
    def check(self):
        if all (p != "" for p in self.positions.values()):
            self.finished == True
            return "Empate!"
        
        pos_marked_X = [p for p, v in self.positions.items() if v == "X"]
        pos_marked_O = [p for p, v in self.positions.items() if v == "O"]
        sequences = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for s in sequences:
            if all (pos in pos_marked_X for pos in s):
                self.finished = True
                return "O jogador X venceu"
            elif all (pos in pos_marked_O for pos in s):
                self.finished = True
                return "O jogador O venceu"
        return None
            
class Player:
    def __init__(self, grid, type_):
        self.grid = grid
        self.type = type_
        self.win = False
    def mark_pos(self, pos):
        self.grid.mark(pos, self.type)
        return self.grid.check()

game = Grid()

opt_player_1 = ""
while opt_player_1 not in ["X", "O"]:
    opt_player_1 = input("Player 1 = vai jogar de \"X\" ou \"O\"?\n\n").upper()
    if opt_player_1 not in ["X", "O"]:
        print("Entrada inválida! Digite apenas X ou O.")

opt_player_2 = "X" if opt_player_1 == "O" else "O"

print(f"\nPlayer 1: {opt_player_1}\nPlayer 2: {opt_player_2}")

player1 = Player(game, opt_player_1)
player2 = Player(game, opt_player_2)

def print_grid(grid):
    p = grid.positions
    print(f"\n{p[1] or 1} | {p[2] or 2} | {p[3] or 3}")
    print("---------")
    print(f"{p[4] or 4} | {p[5] or 5} | {p[6] or 6}")
    print("---------")
    print(f"{p[7] or 7} | {p[8] or 8} | {p[9] or 9}\n")

while game.finished == False:
    print_grid(game)
    pos = input("Player 1, qual posição quer marcar?\n\n")
    res = player1.mark_pos(int(pos))
    if res == None:
        print_grid(game)
        pos = input("Player 2, qual posição quer marcar?\n\n")
        res = player2.mark_pos(int(pos))
        if res != None:
            print(res)
            break
    else:
        print(res)
        break