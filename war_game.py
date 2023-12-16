import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has  {len(self.all_cards)} card"


Player1 = Player('Player_1')
Player2 = Player('Player_2')

New_Deck = Deck()
New_Deck.shuffle()
for item in range(26):
    Player1.add_cards(New_Deck.deal_one())
    Player2.add_cards(New_Deck.deal_one())
game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(Player1.all_cards) == 0:
        print('Player One,out of cards!Player 2 wins')
        game_on = False
        break

    if len(Player2.all_cards) == 0:
        print('Player Two,out of cards!Player 1 wins')
        game_on = False
        break

    # Starting a new round

# two_of_hurts = Card('Hearts','Two')
# print(two_of_hurts.value)

    Player1_cards = []
    Player1_cards.append(Player1.remove_one())
    Player2_cards = []
    Player2_cards.append(Player2.remove_one())

    # at_war
    at_war = True
    while at_war:
        if Player1_cards[-1].value > Player2_cards[-1].value:
            Player1.add_cards(Player1_cards)
            Player1.add_cards(Player2_cards)

            at_war = False
        elif Player2_cards[-1].value > Player1_cards[-1].value:
            Player2.add_cards(Player2_cards)
            Player2.add_cards(Player1_cards)

            at_war = False
        else:
            print('WAR!!!')
            if len(Player1.all_cards) < 3:
                print("Player one unable to declare war")
                print("Player Two Win !!!")
                game_on = False
                break
            elif len(Player2.all_cards) < 3:
                print("Player Two unable to declare war")
                print("Player One Win !!!")
                game_on = False
                break
            else:
                for item in range(3):
                    Player1_cards.append(Player1.remove_one())
                    Player2_cards.append(Player2.remove_one())
