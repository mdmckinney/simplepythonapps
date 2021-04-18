################################
# Michael D. McKinney          #
# Rock, Paper, and Scissors    #
# January 1, 2021              #
################################

import random

print("\n\n\n\n\t\tLet's play Rock, Paper, and Scissors!\n\n\n")

print("You can either type the full word or the first letter of the word.")

program_wins = 0
user_wins = 0
ties = 0

while True:

	program_choice = random.randint(1,3)

	user_choice = input("\nRock, paper, or scissors (or quit)?  ")
	user_choice = user_choice.lower()

	if user_choice == 'rock' or user_choice == 'r':
		user_choice = 1 
	elif user_choice == 'paper' or user_choice == 'p':
		user_choice = 2
	elif user_choice == 'scissors' or user_choice == 's':
		user_choice = 3
	elif user_choice == 'quit' or user_choice == 'q':
		break
	else:
		print("That wasn't a valid move.  Try again.")
		continue

	if user_choice == 1 and program_choice == 1:
		print("You chose Rock and I chose Rock! It's a tie!")
		ties = ties + 1
		continue

	elif user_choice == 1 and program_choice == 2:
		print("You chose Rock and I chose Paper! I win!")
		program_wins = program_wins + 1
		continue

	elif user_choice == 1 and program_choice == 3:
		print("You chose Rock and I chose Scissors! You win!")
		user_wins = user_wins + 1
		continue

	elif user_choice == 2 and program_choice == 1:
		print("You chose Paper and I chose Rock! You win!")
		user_wins = user_wins + 1		
		continue 

	elif user_choice == 2 and program_choice == 2:
		print("You chose Paper and I chose Paper! It's a tie!")
		ties = ties + 1
		continue 

	elif user_choice == 2 and program_choice == 3:
		print("You chose Paper and I chose Scissors! I win!")
		program_wins = program_wins + 1
		continue

	elif user_choice == 3 and program_choice == 1:
		print("You chose Scissors and I chose Rock! I win!")
		program_wins = program_wins + 1
		continue

	elif user_choice == 3 and program_choice == 2:
		print("You chose Scissors and I chose Paper! You win!")
		user_wins = user_wins + 1	
		continue

	elif user_choice == 3 and program_choice == 3:
		print("You chose Scissors and I chose Scissors! It's a tie!")
		ties = ties + 1	
		continue		

print(f"\nGood game!  Score: I won {program_wins} times, you won {user_wins} "
	f"times, and we were tied {ties} times.\n")
