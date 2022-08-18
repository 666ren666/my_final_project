# my_final_project


War card game - break down

MAIN___________________________________________________
choose between signing-in & logging-in
placing a bet 
check if player is out of coins if so, add 1000 coins to player
initialize the game
start the game & update the coins in csv file
choose between: play / quit or leader-board


LEADER  BOARD__________________________________________
find_top_player()
read from file & right to my_list
find top 10 players in my list
find top player in my list
update the top score
remove player from my_list & add him to top_list


LOGIN  SIGNIN_____________________________________________
choose_between_login_and_signin()

sign_in()
create a player
check if the name is already taken()
updae_csv_file_with_new_player()
return player 	

log_in()
create a player
check_if_player_exists_in_csv_file()
	return player


MODULE__________________________________________________
Card class:
init()
initialize suit & color

show()
returns a number and a suit from 2 -14
display()
prints to screen a visual card

Deck class:
init()
initialize card list 
build()
building a full deck of cards 
shuffle()
shuffle the deck 
to_list()
create a list of the deck of cards 

	
PLAY  QUIT  LEADER-BOARD________________________________

play_quit_leaderboard()
choosing between continue playing, quiting the game and showing the leaderboard 


SCORE  UPDATE___________________________________________

find top player()
read from csv file and write to list of all players
find top player and add player top list 
find top 10 players


WAR  GAME  MODULE______________________________________

Game class:
init()
initialize player, full deck, player & dealer decks, bet

start game()
shuffles the deck divides it between the 2 players
draws the cards out of the player & dealer decks
compares the cards
check who wins the game 


is my bet an int()
check if input of the bet is a valid one 

do i have coins()
checks if player has coins 
if he doesn't, add 1000 coins to him
