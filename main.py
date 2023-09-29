import random
from bke import start, EvaluationAgent, MLAgent, is_winner, opponent, train, save, load

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

# Hoofdmenu + loop om het spel opnieuw te kunnen spelen
def menu():
    print()
    print("Welkom bij boter kaas & eieren!")
    print("Kies het spel dat je wilt spelen.")

    i = input("""
                1: Tegen een andere speler spelen
                2: Tegen een makkelijke tegenstander spelen
                3: De tegenstander trainen
                4: Tegen een slimme tegenstander spelen           
                """)

    if i == "1":
        anderpersoon()

    if i == "2":
        domtegen()

    if i == "3":
        trainen()

    if i == "4":
        slimtegen()

def again():
    print()
    again_input = input("Wil je opnieuw spelen? Toets Ja of Nee    ")
    if again_input.lower() == "ja":
        print("")
        menu()
    else:
        print()
        print("Bedankt voor het spelen en tot ziens!")
        quit()

# Functies van de soorten spellen die je kan spelen;

def anderpersoon():
    start()
    again()

def domtegen():
    my_random_agent = MyRandomAgent()
    start(player_o=my_random_agent)
    again()

def trainen():
    my_agent = MyAgent()
    train(my_agent, 3000)
    save(my_agent, 'MyAgent_3000')
    print("De speler is getraind! Als je tegen de getrainde speler wilt spelen kies dan voor opnieuw spelen en kies voor spel 4!")
    print()
    again()

def slimtegen():
    my_agent = load('MyAgent_3000')
    my_agent.learning = False
    start(player_x=my_agent)
    again()

menu()
