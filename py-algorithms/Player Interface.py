from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [(0,0)]

    def make_move(self):
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        new_position = random.choice(self.moves)
        self.position = new_position
        self.path.append(new_position)
        return self.position

    
    @abstractmethod
    def level_up(self):
        pass
        
class Pawn(Player):
    def __init__(self,moves):
        super().__init__()
        self.moves = moves
