import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣︎"]
HAND_SIZE = 10

def build_deck():
    return [f"{card}{suit}" for card in CARDS for suit in SUITS]



def sample(items, count):
    # card_list = []
    # while len(card_list) < count: 
    #     card_index = random.randint(0,len(items) - 1)
    #     if not items[card_index] in card_list:
    #         card_list.append(items[card_index])

    card_list = []        
    deck_copy = list(items)
    for _ in range(10):
        card_index = random.randint(0, len(deck_copy)-1)
        card_list.append(deck_copy[card_index])
        deck_copy.pop(card_index)

    return card_list



# write a function that deals 10 cards from a deck of cards without using the sample function
def deal_ten_cards(deck_of_cards):
    return sample(deck_of_cards, HAND_SIZE)

deck = build_deck()
print(deck)
print(deal_ten_cards(deck))