import random
import os
import time
from collections import Counter
 
# The Card class definition
class Card:
    
    def __init__(self, suit, value, card_value):
         
        # Suit of the Card like Spades and Clubs
        self.suit = suit
 
        # Representing Value of the Card like A for Ace, K for King
        self.value = value
 
        # Score Value for the Card like 10 for King
        self.card_value = card_value
 
if __name__ == '__main__':
    print("is this thing on")
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit value 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # The deck of cards
    deck = []
 
    # Loop for every type of suit
    for suit in suits:
 
        # Loop for every type of card in a suit
        for card in cards:
 
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    total_number_of_cards=len(deck)
    cards_of_2 = sum(i.card_value==2 for i in deck)
    cards_of_3 = sum(i.card_value==3 for i in deck)
    cards_of_4 = sum(i.card_value==4 for i in deck)
    cards_of_5 = sum(i.card_value==5 for i in deck)
    cards_of_6 = sum(i.card_value==6 for i in deck)
    cards_of_7 = sum(i.card_value==7 for i in deck)
    cards_of_8 = sum(i.card_value==8 for i in deck)
    cards_of_9 = sum(i.card_value==9 for i in deck)
    cards_of_10 = sum(i.card_value==10 for i in deck)
    cards_of_11 = sum(i.card_value==11 for i in deck)
    print(cards_of_2)
    print(cards_of_3)
    print(cards_of_4)
    print(cards_of_5)
    print(cards_of_6)
    print(cards_of_7)
    print(cards_of_8)
    print(cards_of_9)
    print(cards_of_10)
    print(cards_of_11)
    print(total_number_of_cards)


     