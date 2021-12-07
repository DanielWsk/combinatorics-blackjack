import random
import os
import itertools
from math import comb
 
# The Card class definition
class Card:
    
    def __init__(self, suit, value, card_value):
         
        # Suit of the Card like Spades and Clubs
        self.suit = suit
 
        # Representing Value of the Card like A for Ace, K for King
        self.value = value
 
        # Score Value for the Card like 10 for King
        self.card_value = card_value
 
# Function that reshuffles deck
def shuffle():
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds", "Spades", "Hearts", "Clubs", "Diamonds"]
 
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

    return deck

# Function that counts deck
def count_deck(deck):
    total_number_of_cards=len(deck)
    cards_of_1 = sum(i.card_value==2 for i in deck)
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
    print("Total number of cards: " + str(total_number_of_cards))

# Function to test probability of blackjack of initial hand
def chances_of_blackjack(deck):
    total_number_of_cards=len(deck)
    cards_of_10 = sum(i.card_value==10 for i in deck)
    cards_of_11 = sum(i.card_value==11 for i in deck)
    total_comb = comb(total_number_of_cards,2)
    comb_of_bj = comb((cards_of_10 * cards_of_11),1)
    probability = comb_of_bj/total_comb
    probability = round(probability * 100, 2)

    print("Your probablity of hitting blackjack is " + str(probability) + "%")
    return probability

# Function for determining chances of busting
def chances_of_busting(deck, players_score):
    for i in deck:
        if i.card_value == 11:
            i.card_value = 1
    margin = 21 - players_score
    safe_cards = sum(i.card_value <= margin for i in deck)
    total_number_of_cards=len(deck)
    danger_cards = total_number_of_cards - safe_cards
    probability = danger_cards/total_number_of_cards
    probability = round(probability * 100, 2)
    print ("Your chances of busting is " + str(probability) + "%")
    return probability

# Function for probability if will be between 12 and 16 of initial hand 
def initial_hand_chances(deck):
    bad_range = 0
    card_values = []
    for i in deck:
        card_values.append(i.card_value)
    for i in itertools.combinations(card_values,2):
        if sum(i) in range(12,17):
            bad_range += 1
    total_number_of_cards=len(deck)
    total_comb = comb(total_number_of_cards,2)
    probability = bad_range/total_comb
    probability = round(probability * 100, 2)
    print ("Your chances of being in the bad zone is " + str(probability) + "%")
    return probability

# Function to see if 3rd card will be between 17 and 21
# def third_card_chances(deck, player_score):
    # to do

# Function for game of blackjack
def blackjack_game(deck):

    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []
 
    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    # Number of rounds won by dealer and player
    global player_rounds_won
    global dealer_rounds_won
    global rounds_tied
    global rounds_skipped
    global rounds_busted

    if blackjack_game.counter == 900:
        print("Player: " + str(player_rounds_won))
        print("Dealer: " + str(dealer_rounds_won))
        print("Tie: " + str(rounds_tied))
        print("Skipped: " + str(rounds_skipped))
        print("Busted: " + str(rounds_busted))
        quit()

    blackjack_game.counter += 1
    print ("Game Number: " + str(blackjack_game.counter))

    count_deck(deck)
    if len(deck) < 15:
            deck = shuffle()

    chances_of_bj = chances_of_blackjack(deck)
    initial_hand = initial_hand_chances(deck)

    if initial_hand > 42:
        rounds_skipped += 1
        random_number = random.randint(4,6)
        for i in range(1, random_number):
            dead_card = random.choice(deck)
            deck.remove(dead_card)
        blackjack_game(deck)

    if len(deck) > 40 and chances_of_bj < 4:
        rounds_skipped += 1
        random_number = random.randint(4,6)
        for i in range(1, random_number):
            dead_card = random.choice(deck)
            deck.remove(dead_card)
        blackjack_game(deck)


    print ("Dealings hands...")
 
    # Initial dealing for player and dealer
    while len(player_cards) < 2:
 
        if len(deck) < 1:
            deck = shuffle()

        # Randomly dealing a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
 
        # Updating the player score
        player_score += player_card.card_value
 
        # In case both the cards are Ace, make the first ace value as 1 
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
 
        # Randomly dealing a card
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer score
        dealer_score += dealer_card.card_value
 
        # In case both the cards are Ace, make the second ace value as 1 
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

    # Player gets a blackjack   
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        player_rounds_won += 1
        blackjack_game(deck)

    chance = 40
    target = 17
 
    # Managing the player moves
    while player_score < 21:
        chance_of_bust = chances_of_busting(deck, player_score)

        if chance_of_bust < chance:

            # Checking size of deck
            if len(deck) < 1:
                deck = shuffle()
 
            # Dealing a new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # Updating player score
            player_score += player_card.card_value
 
            # Updating player score in case player's card have ace in them
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
             
        # If player decides to Stand
        if chance_of_bust >= chance:
            break
 
    # Check if player has a Blackjack
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK")
        player_rounds_won += 1
        blackjack_game(deck)
 
    # Check if player busts
    if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
        rounds_busted += 1
        dealer_rounds_won += 1
        blackjack_game(deck)
 
 
    # Managing the dealer moves
    while dealer_score < 17:

        # Checking size of deck
        if len(deck) < 1:
            deck = shuffle()
 
        # Dealing card for dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer's score
        dealer_score += dealer_card.card_value
 
        # Updating player score in case player's card have ace in them
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1    
 
    # Dealer busts
    if dealer_score > 21:        
        print("DEALER BUSTED!!! YOU WIN!!!") 
        player_rounds_won += 1  
        blackjack_game(deck)
 
    # Dealer gets a blackjack
    if dealer_score == 21:
        print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
        dealer_rounds_won += 1 
        blackjack_game(deck)
 
    # TIE Game
    if dealer_score == player_score:
        print("TIE GAME!!!!")
        rounds_tied +=1
 
    # Player Wins
    elif player_score > dealer_score:
        print("PLAYER WINS!!!") 
        player_rounds_won += 1                 
 
    # Dealer Wins
    else:
        print("DEALER WINS!!!")  
        dealer_rounds_won += 1     

    
    blackjack_game(deck)          
 
if __name__ == '__main__':

    blackjack_game.counter = 0
    # Number of rounds won by dealer and player
    global player_rounds_won
    global dealer_rounds_won
    global rounds_tied
    global rounds_skipped
    global rounds_busted
    player_rounds_won = 0
    dealer_rounds_won = 0
    rounds_tied = 0
    rounds_skipped = 0
    rounds_busted = 0
 
    deck = shuffle()

    
    blackjack_game(deck)    
