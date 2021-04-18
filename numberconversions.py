################################
# Michael D. McKinney          #
# Number Conversions           #
# December 30, 2020            #
################################

print("\n\n\n\t\tNUMBER CONVERSIONS\n\n\n")

while True:
	user_input = input("\nInput a number and I'll convert it into "
		"binary, hexadecimal, and octal. \nType quit to exit. \n")
	user_input = user_input.lower()

	if user_input != 'quit' and user_input != 'qui' and user_input != 'qu' and user_input != 'q':

		try:
			user_input = int(user_input)
		except ValueError:
			print("\nThat wasn't a valid input.  Try again.")
			continue

		print(f"\nThe binary form of {user_input} is {bin(user_input)}.\n")
		print(f"The hexadecimal form of {user_input} is {hex(user_input)}.\n")
		print(f"The octal form of {user_input} is {oct(user_input)}.\n")

		again = input("Do you want to enter another number? ")
		again = again.lower()
		if again == 'yes' or again == 'ye' or again == 'y':
			continue
		elif again == 'no' or again == 'n':
			break
		else:
			print("Going to assume you meant to type no.")
			break			

	elif user_input == 'quit' or user_input == 'qui' or user_input == 'qu' or user_input == 'q':	
		break	

print("\nHave a great day!\n")