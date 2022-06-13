import time
import sys
import random



print("Welcome to Rock Paper Scissors!")
print("-------------------------------")


def win():
    print('THE GAME: You win')
def lost():
    print('THE GAME: You lost')
def tie():
    print('THE GAME: Its a tie')
  
def the_game():
    moves = ['r', 'p', 's']
    print('Choose one: R, P, S?')
    attempts = 3
    while True:
        if attempts == 0:
            print('THE GAME: You failed to provide a correct option')
            time.sleep(5)
            sys.exit(0)

        player = str(input('Player:')).lower()
        if player.lower() not in moves:
            print(f'THE GAME: Invalid option! You have {attempts} attempts left')
            attempts -= 1
        else:
            computer =random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                tie()
            elif player == "r" and computer == "p":
                lost()
            elif player == "r" and computer == "s":
                win()
            elif player == "s" and computer == "p":
                win()
            elif player == "s" and computer == "r":
                lost()
            elif player == "p" and computer == "r":
                win()
            elif player == "p" and computer == "s":
                lost()
            else:
                pass


            #game loop
            play_again = str(input('THE GAME: Retry? (y/n:)'))
            if play_again.lower() == 'y':
                the_game
            elif play_again.lower() =='n':
                print('THE GAME: Game Over. Goodbye.')
                time.sleep(3)
                sys.exit(0)
            else:
                print('THE GAME: Invalid Option. Goodbye')
                time.sleep(2.5)
                sys.exit(0)




if __name__=='__main__':
    the_game()
