import random

def main():
    while True:
        rand = random.randint(1, 10)
        player_1 = int(input("Enter player 1 guess: "))
        player_2 = int(input("Enter player 2 guess: "))
    
        if player_1 > player_2 :
            print("Player 2 wins!")
            print("The number was:", player_2)
        
        elif player_1 == player_2:
            print("Tie!")
        
        else:
            print("Player 1 wins!")
            print("The number was:", player_1)
        q_input = input("Do you want to continue? [y/n]")
        if q_input.lower()[0] == 'n':
            break
main()