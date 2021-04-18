###################################
# Michael D. McKinney             #
# Math Practice (Using functions) #               
# December 31, 2020               #
###################################

#Random number generator.
import random

#Opening
print("\n\n\n\t\tMATH PRACTICE\n\n\n")
print("Let's do some math problems.\n")

#Setting up inital random numbers.
first_number = random.randint(1,100)
second_number = random.randint(1,100)
attempted = 0
solved = 0

# Asking user for input before we enter the while loop.  
choice = input("\nWhich problem to practice? (You can enter the "
			"symbol.) \nAddition (+), Subtraction (-), Multiplication (*), "
			"Division (/), or Quit: ")
choice = choice.lower()

#ADDITION FUNCTION
def addition(first_number, second_number):

	"""ADDITION FUNCTION - Do Addition Problem"""

	print("\nEnter a number or type quit.\n")
	user_input = input(f"{first_number} + {second_number} = ")
	user_input = user_input.lower()

	# User hasn't typed quit, so we're going to go ahead and begin a problem.
	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			user_input = int(user_input)
		except ValueError:
			print("That wasn't a valid input.  Try again.")
			result = 'invalidinput'
			return(result)

		#Compare the integer to see if it matches the sum.
		if user_input == first_number + second_number:
			print("Correct!")
			result = "correct"
			return(result)

		#User input a zero.		
		elif user_input == 0:		
			print("You can't get a zero by adding two non-zero positive numbers"
				". Try again.")
			result = "incorrect"
			return(result)

		#User input a negative number.		
		elif user_input < 0:		
			print("You can't get a negative number by adding two "
				"positive numbers.  Try again. ")
			result = "incorrect"
			return(result)			

		#Incorrect answer.		
		elif user_input != first_number + second_number:		
			print("Incorrect.")
			result = "incorrect"
			return(result)

	# The user opted to quit practicing and return to the menu.
	elif user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':
		result = 'quit'
		return(result)

# MULITPLICATION FUNCTION
def multiplication(first_number, second_number):

	"""MULTIPLICATION FUNCTION - Do Mulitplication Problem"""

	print("\nEnter a number or type quit.\n")
	user_input = input(f"{first_number} * {second_number} = ")
	user_input = user_input.lower()

	# User hasn't typed quit, so we're going to go ahead and begin a problem.
	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			user_input = int(user_input)
		except ValueError:
			print("That wasn't a valid input.  Try again.")
			result = 'invalidinput'
			return(result)

		#Compare the integer to see if it matches the solution.
		if user_input == first_number * second_number:
			print("Correct!")
			result = "correct"
			return(result)

		#User input a zero.		
		elif user_input == 0:		
			print("You can't get a zero by multiplying two non-zero positive "
				"numbers. Try again.")
			result = "incorrect"
			return(result)

		#User input a negative number.		
		elif user_input < 0:		
			print("You can't get a negative number by multiplying two "
				"positive numbers.  Try again. ")
			result = "incorrect"
			return(result)			

		#Incorrect answer.		
		elif user_input != first_number + second_number:		
			print("Incorrect.")
			result = "incorrect"
			return(result)

	# The user opted to quit practicing and return to the menu.
	elif user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':
		result = 'quit'
		return(result)

# SUBTRACTION FUNCTION
def subtraction(first_number, second_number):

	"""SUBTRACTION FUNCTION - Do Subtraction Problem"""

	print("\nEnter a number or type quit.\n")
	user_input = input(f"{first_number} - {second_number} = ")
	user_input = user_input.lower()

	# User hasn't typed quit, so we're going to go ahead and begin a problem.
	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			user_input = int(user_input)
		except ValueError:
			print("That wasn't a valid input.  Try again.")
			result = 'invalidinput'
			return(result)

		#Compare the integer to see if it matches the solution.
		if user_input == first_number - second_number:
			print("Correct!")
			result = 'correct'
			return(result)	

		#Incorrect answer.		
		elif user_input != first_number - second_number:		
			print("Incorrect.  Try again.")
			result = "incorrect"
			return(result)		

	# The user opted to quit practicing and return to the menu.
	elif user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':
		result = 'quit'
		return(result)	

# DIVISION FUNCTION
def division(first_number, second_number):

	"""DIVISION FUNCTION - Do Division Problem"""

	print("\nEnter a number rounded to the nearest 2nd decimal point "
		"or type quit.\n")
	user_input = input(f"{first_number} / {second_number} = ")
	user_input = user_input.lower()

	# User hasn't typed quit, so we're going to go ahead and begin a problem.
	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':

		# Convert input string into integer.
		# Try/Except to catch anything that isn't a number.
		try:
			user_input = float(user_input)
		except ValueError:
			print("That wasn't a valid input.  Try again.")
			result = 'invalidinput'
			return(result)

		#Rounding up the solution to the second decimal place.
		rounded_number = first_number / second_number
		rounded_number = float("%0.2f" % (rounded_number))

		#Compare the integer to see if it matches the solution.
		if user_input == rounded_number:
			print("Correct!")
			result = 'correct'
			return(result)	

				#User input a zero.		
		elif user_input == 0:		
			print("You can't get a zero by dividing two non-zero positive "
				"numbers. Try again.")
			result = "incorrect"
			return(result)

		#User input a negative number.		
		elif user_input < 0:		
			print("You can't get a negative number by dividing two "
				"positive numbers.  Try again. ")
			result = "incorrect"
			return(result)	

		#Incorrect answer.		
		elif user_input != rounded_number:		
			print("Incorrect.  Try again.")
			result = "incorrect"
			return(result)					

	# The user opted to quit practicing and return to the menu.
	elif user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':
		result = 'quit'
		return(result)		

# MAIN PROGRAM LOOP
while True:

	# Menu.  Users will have to type exactly the correct spelling of the term
	# or they could enter the symbol (+, -, *, /) to begin the practice.
	if choice == 'addition' or choice == '+':
		result = addition(first_number, second_number)

	elif choice == 'subtraction' or choice == '-':
		result = subtraction(first_number, second_number)

	elif choice == 'multiplication' or choice == '*':
		result = multiplication(first_number, second_number)

	elif choice == 'division' or choice == '/':
		result = division(first_number, second_number)		

	#The user opted to quit the program.
	elif choice == 'quit' or choice == 'qui' or choice == 'qu' or choice == 'q':
		break

	# Catch all for any inputs that the program doesn't understand.	
	else:
		print("\nI don't understand your input.")
		choice = input("\nWhich problem to practice? (You can enter the "
			"symbol.) \nAddition (+), Subtraction (-), Multiplication (*), "
			"Division (/), or Quit: ")
		choice = choice.lower()
		continue

	# If user answered correctly, offer him option to either
	# continue practicing or quitting to the menu.  
	if result == 'correct':

		# Add one to solved counter. 
		solved = solved + 1

		ask = input("\nWant to try another problem? ")
		if ask == 'yes' or ask == 'ye' or ask == 'y':

			# Generate a new set of numbers.
			first_number = random.randint(1,100)
			second_number = random.randint(1,100)

			continue

		# The user opted to stop practicing and return to the mneu.
		elif ask == 'no' or ask == 'n':
			choice = input("\nWhich problem to practice? (You can enter the "
			"symbol.) \nAddition (+), Subtraction (-), Multiplication (*), "
			"Division (/), or Quit: ")
			choice = choice.lower()

			# Generate a new set of numbers.
			first_number = random.randint(1,100)
			second_number = random.randint(1,100)

			continue

		# User input something that doens't make sense to the program.
		# So the program will assume user wanted to exit the practice 
		# and send them back to the menu. 
		else:
			print("I don't understand your input. Returning you to the menu.")
			choice = input("\nWhich problem to practice? (You can enter the "
			"symbol.) \nAddition (+), Subtraction (-), Multiplication (*), "
			"Division (/), or Quit: ")
			choice = choice.lower()

			# Generate a new set of numbers.
			first_number = random.randint(1,100)
			second_number = random.randint(1,100)

			continue	

	# If the user answered incorrectly, stay on the same problem
	# until the user answered correctly or quit.  
	if result == 'incorrect':
		attempted = attempted + 1
		continue

	# If the user entered invalid input, stay on the same problem
	# until the user answered correctly or quit.  
	#Don't add one to attempted counter.  
	if result == 'invalidinput':
		continue	

	# If the user opted to quit practicing the problem, 
	# send them back to the menu.  
	if result == 'quit':
		choice = input("\nWhich problem to practice? (You can enter the "
			"symbol.) \nAddition (+), Subtraction (-), Multiplication (*), "
			"Division (/) or Quit: ")
		choice = choice.lower()

		# Generate a new set of numbers.
		first_number = random.randint(1,100)
		second_number = random.randint(1,100)
		continue

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