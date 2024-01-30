#classes for mile stone project
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':"depend"}

class card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(card(suit,rank))
    
    def shuffle(self):
        shuffle(self.all_cards)

class player:
    
    def __init__(self,name,money):
        self.name = name
        self.money = money
    
    def collect_money(self,bet):
        self.money += bet
        
    def lose_money(self,bet):
        if self.money >= bet:
            self.money -= bet
        else:
            print("You are broke! There is no money left")