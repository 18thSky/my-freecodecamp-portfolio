import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        new_position = random.choice(self.moves)
        x, y = self.position
        move_x, move_y = new_position
        self.position = (x+move_x, y+move_y)
        self.path.append(self.position)
        return self.position

    
    @abstractmethod
    def level_up(self):
        pass
        
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1), (1,0), (-1,0)]
    def level_up(self):
        self.moves.extend([(1, 1),(-1, 1),(1, -1),(-1, -1)])