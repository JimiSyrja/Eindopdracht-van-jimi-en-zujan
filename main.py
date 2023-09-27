import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot


# import random

# from bke import EvaluationAgent,MLAgent, RandomAgent, is_winner, can_win, opponent, train_and_plot, start, load


# class MyRandomAgent(EvaluationAgent):
#     def evaluate(self, board, my_symbol, opponent_symbol):
#         return random.randint(1, 500)

# class MijnSpeler(EvaluationAgent):
#     def evaluate(self, board, my_symbol, opponent_symbol):
#         getal = 1
#         if board[4] == my_symbol:
#             getal = getal + 5
#         return getal

# class MijnSpeler2(EvaluationAgent):
#     def evaluate(self, board, my_symbol, opponent_symbol):
#         getal = 1
#         if can_win(board, opponent_symbol):
#             getal = getal - 1000
#         return getal

# class MyAgent(MLAgent):
#     def evaluate(self, board):
#         if is_winner(board, self.symbol):
#             reward = 1
#         elif is_winner(board, opponent[self.symbol]):
#             reward = -1
#         else:
#             reward = 0
#         return reward
 
# random.seed(1)
  

# train_and_plot(
#     agent=MyAgent,
#     validation_agent=RandomAgent,
#     iterations=50,
#     trainings=100,
#     validations=1000)

 
# while True:
#     print("Kies een optie:")
#     print("1. Speel tegen willekeurig persoon")
#     print("2. Speel tegen een domme agent")
#     print("3. Speel tegen een slimme agent")
#     print("4. Optie 4")
    
#     keuze = input("Voer het nummer van uw keuze in: ")
#     keuze = int(keuze)
    
#     if keuze == 1:
#         my_random_agent = MyRandomAgent()
#         start(player_x=my_random_agent)
#     elif keuze == 2:
#        mijn_speler = MijnSpeler()
#        start(player_o=mijn_speler, player_x=mijn_speler)
#        pass
#     elif keuze == 3:
#        mijn_speler = MijnSpeler2()
#        start(player_o=mijn_speler, player_x=mijn_speler)
#        pass
#     elif keuze == 4:
#       my_agent = MyAgent(alpha=0.8, epsilon=0.2)
#       random_agent = RandomAgent()
#       start(player_x=my_agent)
#       pass








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

# my_agent = load('MyAgent_3000') 
# my_agent.learning = False
  
my_agent = MyAgent(alpha=0.9, epsilon=0.8)
random_agent = RandomAgent()

train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=1000,
    validations=1000)

from bke import start
start(player_x=my_agent)





