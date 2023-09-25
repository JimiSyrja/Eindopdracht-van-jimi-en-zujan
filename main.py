import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
 
random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
