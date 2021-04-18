################################
# Michael D. McKinney          #
# Division Practice            #
# December 30, 2020            #
################################

#Import the random number generator.
import random

#Opening
print("\n\n\n\t\tDIVISION PRACTICE\n\n\n")
print("Let's do some division problems.")

#Setting variables and generating a random number to start the game.
first_number = random.randint(1,100)
second_number = random.randint(1,100)

#Counter to check if user has at least attempted one problem. 
attempted = 0

#Counter to count the number of times the user had solved the problem. 
solved = 0

#The game loop.
while True:

	#Creating a division problem.
	print("\nEnter a number rounded to the nearest 2nd decimal point "
		"or type quit.\n")
	user_input = input(f"{first_number} / {second_number} = ")

	#Making all inputs lowercase, just in case. 
	user_input = user_input.lower()
	
	#If the user haven't typed quit, continue, otherwise halt the game.
	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':		

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			user_input = float(user_input)
		except ValueError:
			print("That wasn't a valid input.  Try again.")
			continue

		attempted = attempted + 1	

		#Rounding up the solution to the second decimal place. 
		rounded_number = first_number / second_number 
		rounded_number = float("%0.2f" % (rounded_number))

		#Compare the user input to see if it matches the solution.
		if user_input == rounded_number:
			print("Correct!")

			solved = solved + 1

			# Play again?		  			
			playagain = input("\nDo another division problem? (Yes/No): ")

			# Converting input to lower case, just in case. 
			playagain = playagain.lower()

			# If the player entered y, ye, or yes,
			# create a new division problem. 
			if playagain == 'y' or playagain == 'ye' or playagain == 'yes':
				first_number = random.randint(1,100)
				second_number = random.randint(1,100)
				continue
	
			# If the player entered n or no, stop the program.
			elif playagain == 'n' or playagain == 'no':
				break

			# Catch-all for any inputs that isn't yes or no.  
			# Going to assume that it meant "no."
			else:
				print("Going to assume you meant no.")
				break

		#User input a zero.		
		elif user_input == 0:		
			print("You can't get a zero by dividing two non-zero numbers. "
				"Try again. ")
			continue		

		#User input a zero.		
		elif user_input < 0:		
			print("No negative numbers in this practice. Try again.")
			continue				

		#Incorrect answer.		
		elif user_input != rounded_number:		
			print("Incorrect.  Try again.")
			continue

	#If the player typed quit, exit the program.
	if user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':
		break

# Closing.  If the user had tried at least one problem and solved it, tell them 
# "Good practice." and give the number of problems attempted and solved.  
# If the user had tried some problems but haven't solved anything, tell 
# them "Good practice." and give number of attempts. 
# Otherwise, just tell them to come back again.  
if attempted >= 1 and solved != 0:
	print(f"\nGood practice.  "
		f"You attempted to answer {attempted} times and "
		f"solved {solved} problems.")
if attempted >= 1 and solved == 0:
	print(f"\nGood practice.  You attempted to answer {attempted} times.")
print("\nCome back again.\n")