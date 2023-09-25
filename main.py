import random

from bke import MLAgent, RandomAgent, is_winner, opponent, train_and_plot, start, load


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

my_agent = load('MyAgent_3000') 
my_agent.learning = False
 
start(player_x=my_agent)
 
my_agent = MyAgent(alpha=0.8, epsilon=0.2)
random_agent = RandomAgent()

train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

