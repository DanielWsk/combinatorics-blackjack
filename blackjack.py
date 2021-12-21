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
 
# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 
# Function to print the cards
def print_cards(cards, hidden):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()

# Function that reshuffles deck
def shuffle():
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
    print("Cards of 2: " + str(cards_of_2))
    print("Cards of 3: " + str(cards_of_3))
    print("Cards of 4: " + str(cards_of_4))
    print("Cards of 5: " + str(cards_of_5))
    print("Cards of 6: " + str(cards_of_6))
    print("Cards of 7: " + str(cards_of_7))
    print("Cards of 8: " + str(cards_of_8))
    print("Cards of 9: " + str(cards_of_9))
    print("Cards of 10: " + str(cards_of_10))
    print("Cards of 11: " + str(cards_of_11))
    print("Cards of 1: " + str(cards_of_1))
    print("Total number of cards: " + str(total_number_of_cards))

# Function to test probability of blackjack of initial hand
def chances_of_blackjack(deck):
    total_number_of_cards=len(deck)
    cards_of_10 = sum(i.card_value==10 for i in deck)
    cards_of_11 = sum(i.card_value==11 for i in deck)
    total_comb = comb(total_number_of_cards,2)
    comb_of_bj = comb((cards_of_10 * cards_of_11),1)
    probability = comb_of_bj/total_comb
    probability = str(round(probability * 100, 2))

    print("Your probablity of hitting blackjack is " + probability + "%")

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
    probability = str(round(probability * 100, 2))
    print ("Your chances of busting is " +probability + "%")

# Function for probability if will be between 12 and 16 of initial hand 
def initial_hand_chances(deck):
    bad_range = 0
    card_values = []
    for i in deck:
        card_values.append(i.card_value)
    count_deck(deck)
    print (card_values)
    for i in itertools.combinations(card_values,2):
        if sum(i) in range(12,17):
            bad_range += 1
    total_number_of_cards=len(deck)
    total_comb = comb(total_number_of_cards,2)
    probability = bad_range/total_comb
    probability = str(round(probability * 100, 2))
    print("The bad zone is: " + str(bad_range))
    print("The total is: " + str(total_comb))
    print ("Your chances of being in the bad zone is " +probability + "%")

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

    if blackjack_game.counter == 3:
        print("You won " + str(player_rounds_won) + " times!")
        print("The dealer won " + str(dealer_rounds_won) + " times!")
        quit()

    blackjack_game.counter += 1
    print ("Game Number: " + str(blackjack_game.counter))

    chances_of_blackjack(deck)
    initial_hand_chances(deck)

    to_play = input("Would you like to play the hand? Y/N: ")
    if to_play.upper() == "N":
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
 
    # Print dealer and player cards
    print("DEALER CARDS: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
    print() 
 
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    # Player gets a blackjack   
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        player_rounds_won += 1
        blackjack_game(deck)
 
    # Managing the player moves
    while player_score < 21:
        chances_of_busting(deck, player_score)
        choice = input("Enter H to Hit or S to Stand : ")
 
        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Wrong choice!! Try Again")
 
        # If player decides to HIT
        if choice.upper() == 'H':

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
 
            clear()     
 
            # Print player and dealer cards
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
            print()
 
            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)
             
        # If player decides to Stand
        if choice.upper() == 'S':
            break
 
 
    clear() 
 
    # Print player and dealer cards
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)
 
    print()
    print("DEALER IS REVEALING THE CARDS....")
 
    print("DEALER CARDS: ")
    print_cards(dealer_cards, False)
    print("DEALER SCORE = ", dealer_score)
 
    # Check if player has a Blackjack
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK")
        player_rounds_won += 1
        blackjack_game(deck)
 
    # Check if player busts
    if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
        dealer_rounds_won += 1
        blackjack_game(deck)
 
    input() 
 
    # Managing the dealer moves
    while dealer_score < 17:
        clear() 
 
        print("DEALER DECIDES TO HIT.....")

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
 
        # print player and dealer cards
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)
 
        print()
 
        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)      
 
        input()
 
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
    player_rounds_won = 0
    dealer_rounds_won = 0
 
    deck = shuffle()

    clear()
    blackjack_game(deck)    
