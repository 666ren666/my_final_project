from module import Card
############################################################################################################# GAME CLASS



class Game:

    def __init__(self, deck, player_info, bet):
        self.player_info = player_info
        self.deck = deck
        self.player_1 = []
        self.player_2 = []
        self.bet = bet

    def start_game(self, deck):
        deck.shuffle()
        all_cards = deck.to_list()

        counter = 1
        for i in range(52):
            popped_card = all_cards.pop(-1)
            if counter % 2 == 0:
                self.player_1.append(popped_card)
                counter += 1
            else:
                self.player_2.append(popped_card)
                counter += 1

        player_1_hand = self.player_1
        player_2_hand = self.player_2

########################################################################################################################

        while True:

######################################################################################################### CHECK WHO WINS

            if player_1_hand == []:
                print("YOU LOSE :(")
                # print(self.player_info)
                updated_score = int(self.player_info[0])
                print(self.bet)
                self.player_info[0] = updated_score
                player_x = f"{self.player_info[0]},{self.player_info[1]},{self.player_info[2]}"
                print(f"\n\nYou now have: {self.player_info[0]} coins\n")
                return player_x

            if player_2_hand == []:
                print("!!!YOU WIN!!!")
                # print(self.player_info)
                updated_score = int(self.player_info[0]) + (self.bet * 3)
                self.player_info[0] = updated_score
                player_x = f"{self.player_info[0]},{self.player_info[1]},{self.player_info[2]}"
                print(f"\n\nYou now have: {self.player_info[0]} coins\n")
                return player_x


############################################################################################################# DRAW CARDS

            a = player_1_hand.pop(-1)
            b = player_2_hand.pop(-1)

            aa = str(a)
            aaa = aa.split(" ")
            ac = Card(aaa[2], aaa[0])
            acc = ac.display()
            print(acc)

            bb = str(b)
            bbb = bb.split(" ")
            bc = Card(bbb[2], bbb[0])
            bcc = bc.display()
            print(bcc)

            a_card = str(a)
            a_card_split = a_card.split(" ")
            a_val = int(a_card_split[0])
            # print(a_val)

            b_card = str(b)
            b_card_split = b_card.split(" ")
            b_val = int(b_card_split[0])
            # print(b_val)

########################################################################################################## COMPARE CARDS

            if a_val > b_val:
                print("YOU WON THE ROUND")
                player_1_hand.append(a)
                player_1_hand.append(b)

            if a_val < b_val:
                print("YOU LOST THE ROUND")
                player_2_hand.append(a)
                player_2_hand.append(b)


            if a_val == b_val:
                print("!!!WAR!!!")
                c, d = a, b

                if player_1_hand == [] or player_2_hand == []:
                    continue

                a = player_1_hand.pop(-1)
                b = player_2_hand.pop(-1)
                if a_val > b_val:
                    print("YOU WON THE WAR")
                    player_1_hand.append(a)
                    player_1_hand.append(b)
                    player_1_hand.append(c)
                    player_1_hand.append(d)

                if a_val < b_val:
                    print("YOU LOST THE WAR")
                    player_2_hand.append(a)
                    player_2_hand.append(b)
                    player_2_hand.append(c)
                    player_2_hand.append(d)


def is_my_bet_an_int(player_1):

    # check for correct amount of coins
    while True:
        # check for correct input
        while True:

            print("     Press 1: to bet 1 coin \n     Press 2: to bet 5 coins  \n     Press 3: to bet 10 coins \n     Press 4: to bet 50 coins \n     Press 5: to bet 100 coins ")
            placed = input("How many coins would you like to bet?")

            if placed == "1":
                a_bet = 1
                break
            if placed == "2":
                a_bet = 5
                break
            if placed == "3":
                a_bet = 10
                break
            if placed == "4":
                a_bet = 50
                break
            if placed == "5":
                a_bet = 100
                break
            else:
                print("\nwrong input")
                continue

        if int(player_1[0]) - a_bet >= 0:
            return int(a_bet)

        if int(player_1[0]) - a_bet < 0:
            print("\nYou don't enough coins, Please try again\n")
            continue

        else:
            print("Wrong choice entered, Please try again\n")
            continue

def do_i_have_coins(player_1):
    if 0 >= int(player_1[0]):
        player_1[0] = int(player_1[0]) + 1000
        print("Your coins have been re-filled")
