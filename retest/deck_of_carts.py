import random


class Card:
    suit = ''
    value = ''

    def __init__(self, suit='Spade', value='Q'):
        self.suit=suit
        self.value=value


    def __str__(self):
        return f'{self.suit} {self.value}'

class Deck:
    def __init__(self):
        self.cards=[Card('','Joker')]
        for x in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            for i in ["♠","♥","♦","♣"]:
                card=Card(i,x)
                self.cards.append(card)
        

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self, num=-1):
        return self.cards[num]
    
    def random(self):
        return random.choice(self.cards)
    


def run_some_tests():
    "Define a deck and run some tests!"

    deck = Deck()
    print(deck.pop())
    deck.shuffle()
    print(deck.pop())
    print(deck.pop(23))
    print([str(deck.random()) for i in range(5)])
    
run_some_tests()
                          