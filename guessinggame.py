################################
# Michael D. McKinney          #
# Game - Guess the Number      #
# December 29, 2020            #
################################

#Import the random number generator.
import random

#Opening
print("\n\n\n\t\tGUESS THE NUMBER\n\n\n")
print("\nLet's play a game!\n")
print("I'll think of a number between 1 to 25, "
	"and I'll let you guess what it is!")

#Generating a random number to start the game.
number = random.randint(1,25)

#Setting counters at zero.
guess_counter = 0
invalid_entries_counter = 0

#The game loop.
while True:

	#Have the user guess a number.
	guess = input("\nGuess a number, or type quit to stop playing: ")

	#Making all inputs lowercase, just in case. 
	guess = guess.lower()
	
	#If the user haven't typed quit, continue to play, otherwise halt the game.
	if guess != 'quit' and guess != 'qui' and guess != 'qu' and guess != 'q':		

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			guess = int(guess)
		except ValueError:
			print("Oops! That wasn't a number!")
			invalid_entries_counter += 1
			continue

		#Compare the integer to see if it matches the random number.
		if guess == number:
			guess_counter += 1
			print("Correct!")
			print(f"\nYou guessed the number in {guess_counter} turns!")

			# Invalid entries counter.
			if invalid_entries_counter != 0 and invalid_entries_counter == 1:
				print(f"\nYou also entered invalid input "
					  f"{invalid_entries_counter} time.")
			if invalid_entries_counter != 0 and invalid_entries_counter > 1:
				print(f"\nYou also entered invalid input "
					  f"{invalid_entries_counter} times.")	

			# Play again?		  			
			playagain = input("\nPlay again? (Yes/No): ")

			# Converting input to lower case, just in case. 
			playagain = playagain.lower()

			# If the player entered y, ye, or yes, reset the counters
			# and start a new round of guessing game. 
			if playagain == 'y' or playagain == 'ye' or playagain == 'yes':
				number = random.randint(1,25)
				guess_counter = 0
				invalid_entries_counter = 0
				continue
	
			# If the player entered n or no, stop the game.
			elif playagain == 'n' or playagain == 'no':
				break

			# Catch-all for any inputs that isn't yes or no.  
			# Going to assume that it meant "no."
			else:
				print("Going to assume you meant no.")
				break

		#Guessed a number that's too high.		
		if guess > number and guess <= 25:
			guess_counter += 1			
			print("Too high!")
			continue

		# Player had entered a number that's higher than 25.
		if guess > number and guess > 25:
			print("Please pick only numbers between 1 and 25!")
			invalid_entries_counter += 1
			continue

		#Guessed a number that's too low.	
		if guess < number and guess > 0:
			guess_counter += 1
			print("Too low!")
			continue

		# Player had entered a number that's lower than 1.
		# Including negative numbers.
		if guess < number and guess <= 0:
			print("Please pick only numbers between 1 and 25!")
			invalid_entries_counter += 1
			continue	

	#If the player typed quit, exit the game.
	if guess == 'quit' or guess == 'qui' or guess == 'qu' or guess == 'q':
		break

# Farewell message.  If player attempted at least one guess, print "Good Game!"
# and "Come again!"  Otherwise, just print only "Come again!"
if guess_counter != 0:
	print(f"\nGood game!")
print("\nCome again!\n")