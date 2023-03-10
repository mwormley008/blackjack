## Blackjack program

import random

table = []

class Game:
    # Ok so this game is going to need 2 players, a dealer and a player, a deck of cards, and rules I guess?
    pass


class Deck:
    #The deck will begin the game shuffled and have all the cards in the deck
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    # Each card is going to have a value and a suit
    # Each card needs to be given a value and a suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + ' of ' + self.suit


class Human:
    # Each human will have a hand of cards and the ability to hit or stay (unless the dealer doesn't have that ability)
    def __init__(self, name):
        self.hand = []
        self.name = name

    def hit(self, deck):
        #human is passed a card, I think I want to generate the card as the the top of the deck
        card = deck.cards.pop(0)
        self.hand.append(card)

    def stay(self):
        pass

    def __str__(self):
        return self.name


class Dealer(Human):
    # The dealer will only be able to play after the human
    def __init__(self, name):
        super().__init__(name)  # Call the __init__ method of the parent class
        table.append(self)
    # def deal(deck):
    #     for seated at table:
    #         seated.hit(deck)
    pass

    def __str__(self):
        return self.name

# the player can hit or stay (perhaps more to come)
class Player(Human):
    def __init__(self, name):
        super().__init__(name)  # Call the __init__ method of the parent class
        table.append(self)

def main():
    #This defines the main function of the program
    if __name__=="__main__":
        print("Hello, world!")
        #Shuffle the cards when the game begins
        

main()
        
Jeff, George = Player('Jeff'), Dealer('George')
main_deck = Deck()
main_deck.shuffle()
print([str(card) for card in main_deck.cards])
for seated in table:
    print(str(seated))
Jeff.hit(main_deck)
Jeff.hit(main_deck)

print([str(card) for card in Jeff.hand])
print([str(card) for card in main_deck.cards])
