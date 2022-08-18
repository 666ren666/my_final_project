from login_signin import choose_between_login_and_signin
from module import Deck
from war_game_module import Game, is_my_bet_an_int, do_i_have_coins
from play_quit_leaderboard import play_quit_leaderboard

# CHOOSE BETWEEN : SIGN IN & LOG IN
player_1 = choose_between_login_and_signin()

print(f"\n\n\nHello {player_1[1]} \nYou have: {player_1[0]} coins")
start_game = input("PRESS ENTER TO START")

while True:

    # PLACE YOUR BET
    bet = is_my_bet_an_int(player_1)
    player_1[0] = int(player_1[0]) - bet

    # CHECK IF PLAYER IS OUT OF COINS, IF SO: ADD 1000 COINS TO PLAYER
    do_i_have_coins(player_1)

    # INITIALIZE THE GAME
    my_deck = Deck()
    war = Game(my_deck, player_1, bet)

    # START GAME & UPDATE COINS IN CSV FILE
    player_with_new_score = war.start_game(my_deck)

    # CHOOSE BETWEEN : PLAY / QUIT or LEADER-BOARD
    a = play_quit_leaderboard(player_1, player_with_new_score)
    if a == "end game":
        break
