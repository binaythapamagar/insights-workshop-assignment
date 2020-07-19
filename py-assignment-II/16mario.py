
class Mario:
    
    def __init__(self,player_name):
        self.player_name = player_name
        
    def startGame(self):
        self.score = 0
    
    def addCoin(self):
        self.score +=1
        print(f'Your score is {self.score}')
    
    def die(self):
        print(f'Your final score is {self.score}')
    
if __name__ == "__main__":
    mario = Mario('mario')
    mario.startGame()
    mario.addCoin()
    mario.addCoin()
    mario.die()