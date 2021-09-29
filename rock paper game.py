"""6. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start
a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock"""

print("WELCOME TO ROCK, PAPER, SCISSORS GAME")
player1 = str(input("enter the choice player1: "))
player2 = str(input("enter the choice player2: "))
def game(player1,player2):
    a_list=["rock","paper","scissors"]

    if player1 == "rock" and player2 == "scissors":
        print("player1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("player1 wins!")
    elif player2 == "rock" and player1 == "scissors":
        print("player2 wins!")
    elif player2 == "scissors" and player1 == "paper":
        print("player2 wins!")
    elif player2 == "paper" and player1 == "rock":
        print("player2 wins!")

game(player1, player2)
play_again = str(input("want to play again? type y if you want to continue playing"))

while play_again == "y":
    player1 = str(input("enter the choice player1: "))
    player2 = str(input("enter the choice player2: "))
    game(player1, player2)
    play_again = str(input("want to play again? type y if you want to continue playing"))