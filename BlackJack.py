## Blackjack program

import random

table = []

class Game:
    
    def __init__(self):
        self.players = []
        self.turn = 'player'
        self.deck = Deck()
        self.deck.shuffle()
        self.game_over = False
        self.dealer = Dealer('George', self)

    def add_player(self, player_name):
        player = Human(player_name, self)
        self.players.append(player)

    def change_turn(self):
        ## start with player's turn, then when this function is called, it's the dealer's turn
        self.turn = 'dealer'

    def win(self, player):
        dealer_score = self.dealer.handvalue
        if player.handvalue > 21:
            return f"{player.name} busted! Dealer wins!"
        elif dealer_score > 21:
            return f"{player.name} wins! Dealer busted!"
        elif player.handvalue > dealer_score:
            return f"{player.name} wins!"
        elif player.handvalue == dealer_score:
            return f"{player.name} and dealer tied!"
        else:
            return f"Dealer wins!"

    def lose_check(self, current_player):
        if current_player.handvalue > 21:
            print(f"{current_player.name} went bust.")
            self.change_turn()
            return True
        elif current_player.handvalue == 21:
            print(f"Blackjack!")
            self.win(current_player)
        else:
            return False

    def play(self):
        scorelist = {}
        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)
            print(f"{player.name} has: {[str(card) for card in player.hand]}")
            print(f"{player.name}'s total score is: {player.handvalue}")
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.see_dealer_hand()
        self.players.append(self.dealer)
        while self.turn == 'player':
            current_player = self.players[0]
            print(f"It's {current_player.name}'s turn.")
            if self.lose_check(current_player) == False:
                choice = input("Do you want to hit or stay? ")
                if choice.lower() == 'hit':
                    current_player.hit(self.deck)
                    print(f"{current_player.name} has: {[str(card) for card in current_player.hand]}")
                    print(f"{current_player.name}'s total score is: {current_player.handvalue}")
                    self.lose_check(current_player)
                elif choice.lower() == 'stay':
                    current_player.stay(current_player)

                    
                
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
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + ' of ' + self.suit


class Human:
    # Each human will have a hand of cards and the ability to hit or stay (unless the dealer doesn't have that ability)
    def __init__(self, name, game):
        self.hand = []
        self.handvalue = 0
        self.name = name
        self.game = game

    def hit(self, deck):
        #human is passed a card, I think I want to generate the card as the the top of the deck
        card = deck.cards.pop(0)
        self.hand.append(card)
        if card.value in ['J', 'Q', 'K']:
            self.handvalue += 10
        elif card.value == 'A':
            if self.handvalue + 11 > 21:
                self.handvalue += 1
            else:
                self.handvalue += 11
        else:
            self.handvalue += int(card.value)
        # Calculate if the player has hit 21 or has gone bust
        
    def display_hand(self):
        print(f"{self.name}'s hand is {[str(card) for card in self.hand]}")

    def stay(self, current_player):
        scorelist = {}
        print(f"{self.name} chooses to stay.")
        scorelist[current_player.name] = current_player.handvalue
        self.game.change_turn()
        while self.game.turn == 'dealer':
            self.game.dealer.display_hand()
            while self.game.dealer.handvalue < 17:
                self.game.dealer.hit(self.game.deck)
                self.game.dealer.display_hand()
                print(f"{self.game.dealer.name}'s total score is: {self.game.dealer.handvalue}")
            self.game.game_over = True
            print(self.game.win(current_player))
            self.game.turn = 'complete'

    def __str__(self):
        return self.name


class Dealer(Human):
    
    def __init__(self, player_name, game):
        super().__init__(player_name, game)  
        table.append(self)
    
    
    def deal(self, deck):
        for seated in table:
            seated.hit(deck)
        for seated in table:
            seated.hit(deck)
    
    def see_dealer_hand(self):
        print(f"The dealer is showing a {str(self.hand[0])}.")

    def display_hand(self):
        print(f"{self.name}'s hand is {[str(card) for card in self.hand]}")


    def __str__(self):
        return self.name


class Player(Human):
    def __init__(self, name, game):
        super().__init__(name, game)  
        table.append(self)


def main():
    game = Game()
    Jeff = Player('Jeff', game)
    game.add_player(Jeff)
    game.play()
    
        
main()
        
