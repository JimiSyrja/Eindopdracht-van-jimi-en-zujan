import random

from bke import (
    EvaluationAgent,
    MLAgent,
    RandomAgent,
    is_winner,
    load,
    opponent,
    plot_validation,
    save,
    start,
    train,
    train_and_plot,
    validate,
)


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
                5: De validatie grafiek plotten
                """)

    if i == "1":
        anderpersoon()

    if i == "2":
        domtegen()

    if i == "3":
        trainen()

    if i == "4":
        slimtegen()
    
    if i == "5":
        plot()


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
    print("De speler is getraind! Als je tegen de getrainde speler wilt                 spelen kies dan voor opnieuw spelen en kies voor spel 4!")
    print()
    again()

def slimtegen():
    my_agent = load('MyAgent_3000')
    my_agent.learning = False
    start(player_x=my_agent)
    again()

def plot():
  random.seed(1)
 
  my_agent = MyAgent(alpha=0.95, epsilon=0.01)
  #Alpha en epsilon zijn hyperparameters. Met alpha kan je bepalen hoe snel de agent zijn nieuwe kennis gebruikt en zijn oude kennis daarmee vervangt. Met epsilon kan je bepalen hoe vaak de agent een nieuwe strategie probeert in plaats van de beste strategie die hij al kent. Voor beide hyperparameters kan je een getal invullen van 0 tot 1. Hoe hoger het getal voor alpha hoe vaker hij zijn oude kennis zal vervangen. Hoe hoger het getal voor epsilon, hoe vaker hij een nieuwe strategie zal proberen.

  print("De grafiek wordt gemaakt, bedankt voor het spelen!")
  random_agent = RandomAgent()
 
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=100,
      trainings=200,
      validations=1000)
  # de agent wordt hier getraind

  validation_agent = RandomAgent()

  validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
    # laat de agent tegen een randon agent spelen
  
  plot_validation(validation_result)
  again()

menu()