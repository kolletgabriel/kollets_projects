from random import choice
from string import ascii_uppercase

class Deck(object):
    
    cards = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
                  
    @staticmethod
    def random_card():
        return choice(list(Deck.cards.keys()))

class Player(object):
    
    def __init__(self, name, budget=1000.00, hand=[], hand_value=0):
        self.name = name
        self.budget = budget
        self.hand = hand
        self.hand_value = hand_value
    
    def pick_card(self): 
        self.hand_value = 0 #O CONTADOR PRECISA SER ZERADO A CADA EXECUÇÃO, SENÃO ACUMULA OS VALORES ANTERIORES NO ATRIBUTO
        self.hand.append(Deck.random_card())
        for i in self.hand:
            self.hand_value += Deck.cards[i]
        if 'A' in self.hand and self.hand_value <= 11:
            self.hand_value += 10
        if self.hand_value > 21:
            print(50*'-')
            print("Your hand: {}".format(p1.hand))
            print("Bursted! Your actual budget is R$ {:.2f}".format(p1.budget))
            print(50*'-')
            restart_game()
        
    def gamble(self, value):
        self.budget -= value


class Dealer(object):
    
    hand = []
    hand_value = 0
    
    @staticmethod
    def pick_card():
        Dealer.hand_value = 0 
        Dealer.hand.append(Deck.random_card())
        for i in Dealer.hand:
            Dealer.hand_value += Deck.cards[i]
        if 'A' in Dealer.hand and Dealer.hand_value <= 11:
            Dealer.hand_value += 10
        if Dealer.hand_value > 21:
            print("Dealer's hand: {}".format(Dealer.hand))
            p1.budget += bet_value * 1.5
            print("Dealer bursted! You won R$ {}. Your actual budget is R$ {}".format(bet_value * 1.5, p1.budget))
            print(50*'-')
            restart_game()
            
    @staticmethod
    def get_cards():
        while Dealer.hand_value < 17:
            Dealer.pick_card()
        print("Dealer's hand: {}".format(Dealer.hand))

def start_game():
    
    def pick_pass():
        while True:
            try:
                check = input("Want to pick a card? (y / n): ")
                if check == 'y':
                    p1.pick_card()
                    print("Your hand: {}".format(p1.hand))
                    print(50*'-')
                elif check == 'n':
                    print(50*'-')
                    break
                else:
                    raise ValueError('You must digit only "y" or "n"!\n')
            except ValueError:
                print('You must digit only "y" or "n"!\n')
        pass
    
    def player_gamble():
        global bet_value
        bet_value = 0 #O CONTADOR PRECISA SER ZERADO A CADA EXECUÇÃO, SENÃO ACUMULA OS VALORES ANTERIORES NO ATRIBUTO
        while True:
            try:
                bet_value = float(input("Do your bet (R$ {:.2f} balance): ".format(p1.budget)))
                if bet_value > p1.budget:
                    raise ValueError
                else:
                    p1.gamble(bet_value)
                    break
            except ValueError:
                print("You must do a valid bet. Please, insert a number lower or equal than you budget's value.\n",50*'-')
    
    if p1.budget > 0:
        player_gamble()
        p1.pick_card()
        p1.pick_card()
        Dealer.pick_card()
        Dealer.pick_card()
        print(50*'-')
        print("Your hand: {}".format(p1.hand))
        print("Dealer's hand: {}".format(['?',Dealer.hand[-1]]))
        print(50*'-')
        pick_pass()
        Dealer.get_cards()
        comparsion()
    else:
        print("You don't have any value to bet. Goodbye!")
        exit()

def restart_game():
    p1.hand = []
    p1.hand_value = 0
    Dealer.hand = []
    Dealer.hand_value = 0
    start_game()

def comparsion():
    
    def is_blackjack(hand): #DEFINE O "VERDADEIRO" BLACKJACK - UM ÁS E OUTRA LETRA
        if len(hand) == 2 and 'A' in hand and hand[0] != hand[1] and hand[0] in list(ascii_uppercase) and hand[1] in list(ascii_uppercase):
            return True
        else:
            return False
    
    if is_blackjack(p1.hand) is True and is_blackjack(Dealer.hand) is True:
        print("Drawn.")
        p1.budget += bet_value
        print("You won R$ {}. Your actual budget is R$ {}".format(bet_value, p1.budget))
        print(50*'-')
        restart_game()
    elif is_blackjack(p1.hand) is True and is_blackjack(Dealer.hand) is False:
        print("It's a blackjack for you!")
        p1.budget += bet_value * 2
        print("You won R$ {:.2f}. Your actual budget is R$ {:.2f}".format(bet_value * 2, p1.budget))
        print(50*'-')
        restart_game()
    elif is_blackjack(p1.hand) is False and is_blackjack(Dealer.hand) is True:
        print("Blackjack for the Dealer! You lost.")
        print("Your actual budget is R$ {:.2f}".format(p1.budget))
        print(50*'-')
        restart_game()
    elif p1.hand_value == Dealer.hand_value:
        print("Drawn.")
        p1.budget += bet_value
        print("You won R$ {:.2f}. Your actual budget is R$ {:.2f}".format(bet_value, p1.budget))
        print(50*'-')
        restart_game()
    elif p1.hand_value > Dealer.hand_value:
        print("You won!")
        p1.budget += bet_value * 1.5
        print("You won R$ {:.2f}. Your actual budget is R$ {:.2f}".format(bet_value * 1.5, p1.budget))
        print(50*'-')
        restart_game()
    elif p1.hand_value < Dealer.hand_value:
        print("You lost.")
        print("Your actual budget is R$ {:.2f}".format(p1.budget))
        print(50*'-')
        restart_game()

print("----- KOLLET'S BLACKJACK -----\n         (v1.0 alpha)\n")
p1 = Player('Gabriel')
start_game()
