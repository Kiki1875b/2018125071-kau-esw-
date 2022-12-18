

class GameOver:
    def __init__(self): 
        self.state = False
    def check(self, character):
        if character.life <= 0:
            self.state = True
