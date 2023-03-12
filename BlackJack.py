## Blackjack program

import random

table = []

class Game:
    def change_turn(self):
        if turn_count == 0:
            turn_count = 1
        else:
            turn_count = 0
    pass
    #Maybe a game.win function that compares the score to 21


class Deck:
    #The deck will begin the game shuffled and have all the cards in the deck
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']

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
        self.handvalue = 0
        self.name = name

    def hit(self, deck):
        #human is passed a card, I think I want to generate the card as the the top of the deck
        card = deck.cards.pop(0)
        self.hand.append(card)
        self.handvalue += int(card.value)
        # Calculate if the player has hit 21 or has gone bust
        
        

    def stay(self):
        # the player needs the option to stay so that they can stop hitting but the dealer doesn't need that method I am pretty sure
        # this will also pass the turn
        pass

    def __str__(self):
        return self.name


class Dealer(Human):
    # The dealer will only be able to play after the human
    def __init__(self, name):
        super().__init__(name)  # Call the __init__ method of the parent class
        table.append(self)
    
    # One thing I will need to figure out is how to hide the second value of the card 
    def deal(self, deck):
        for seated in table:
            seated.hit(deck)
        for seated in table:
            seated.hit(deck)
    
    def see_dealer_hand(self):
        print(f"The dealer is showing a {str(self.hand[0])}.")

    def __str__(self):
        return self.name

# the player can hit or stay (perhaps more to come)
class Player(Human):
    def __init__(self, name):
        super().__init__(name)  # Call the __init__ method of the parent class
        table.append(self)

    def hit(self, deck):
        #human is passed a card, I think I want to generate the card as the the top of the deck
        card = deck.cards.pop(0)
        self.hand.append(card)
        self.handvalue += int(card.value)
        print(card)
        print(self.handvalue)
        if self.handvalue > 21:
            print("You have gone bust.")
        elif self.handvalue == 21:
            print("You have won the game.")

def main():
    #This defines the main function of the program
    if __name__=="__main__":
        Jeff, George = Player('Jeff'), Dealer('George')
        turn = 0
        main_deck = Deck()
        main_deck.shuffle()
        print([str(card) for card in main_deck.cards])
        for seated in table:
            print(str(seated))
        George.deal(main_deck)
        print([str(card) for card in Jeff.hand])
        # print([str(card) for card in George.hand])
        print([str(card) for card in main_deck.cards])
        George.see_dealer_hand()
        # I'm going to start programming a game here because I don't really want to ask for inputs I'd rather do a gui but we'll see
        
        Jeff.hit(main_deck)
        
main()
        
