# LOTTERY
# Michael McKinney
# January 21, 2021
# Created to show that it's futile to partake in lottery.  
#
# Once a ticket has been created, the program will continuously do lotteries 
# until there is a match.  Then the program will output the number of draws it 
# had to do before there is a match.
#
# Ticket / match only need to have the same numbers, not necessarily in the 
# same order.  Similar to real lottery.
#
# The user can set several variables and see how it affects their odd of 
# winning the lottery.
#
# WARNING - Entering a very high range and selecting more than 3 or 4 numbers
# on the ticket would cause the program to execute for a long time as it try to 
# get a match.  Just like real lottery.  
#

from random import randint
from os import system, name 

def clear(): 
  
    # Windows
    if name == 'nt': 
        _ = system('cls') 
  
    # Mac and Linux 
    else: 
        _ = system('clear') 


class Lottery:
	def __init__(self):
		self.ticket = []
		self.lownumber = 0
		self.highnumber = 0
		self.ticketnumber = 0

		# Preparing for the lottery game by clearing the screen.
		clear()
		print("\t\t-----------------------------------------------")
		print("\n\t\t\t\t   LOTTERY\n")
		print("\t\t-----------------------------------------------")
		print("\t\t\t(Press 'q' at any time to quit.)")

	def build_ticket(self):

		""" Building a lottery ticket. """

		print("\nEnter the range of numbers that can be drawn from the "
			  "pot.")
		while True:
			low = input("Lowest number: ")
			if low == '':
				print("Please enter a number.")
				continue
			elif low == 'q' or low == 'Q':
				exit()
			else:
				try:
					self.lownumber = int(low)
				except:
					print("Please enter a number.")
					continue

			high = input("Highest number: ")
			if high == '':
				print("Please enter a number.")
				continue
			elif high == 'q' or high == 'Q':
				exit()
			else:
				try:
					high = int(high)
					if self.lownumber >= high:
						print("Lowest number can't be higher than Highest "
							  "number.")
						continue
					else:
						self.highnumber = high
						break
				except:
					print("Please enter a number.")
					continue

		while True:
			numberstopick = input("\nHow many numbers on the ticket? ")
			if numberstopick == '':
				print("Please enter a number.")
				continue
			elif numberstopick == 'q' or numberstopick == 'Q':
				exit()
			else:
				try:
					numberstopick = int(numberstopick)
					if numberstopick > self.highnumber:
						print("Number can't exceed the range you set.")
						continue
					else:
						self.ticketnumber = numberstopick
						break
				except:
					print("Please enter a number.")
					continue

		print("\nEnter your ticket number, using the ranges you selected.")
		while True:

			ticketloop = 1
			while len(self.ticket) != self.ticketnumber:
				ticketselection = input(f"Enter number #{ticketloop}: ")
				if ticketselection == '':
					print("Please enter a number.")
					continue
				elif ticketselection == 'q' or ticketselection == 'Q':
					exit()
				else:
					try:
						ticketselection = int(ticketselection)
						if ticketselection > self.highnumber:
							print("Please stay within the ranges you set.")
						elif self.lownumber > ticketselection:
							print("Please stay within the ranges you set.")
						elif ticketselection not in self.ticket:
							self.ticket.append(ticketselection)
							ticketloop += 1
						else:
							print("You can't use the same number more than "
								  "once.")
							continue
					except:
						print("Please enter a number.")
						continue
			break

		return


	def drawings(self):

		""" Playing the lottery game using the ticket we built earlier. """

		repeatdrawing = 0
		drawingresult = []

		print(f"\nYour ticket numbers: {self.ticket}")

		print("\nRapidly playing hundreds/thousands/millions/billions of " 
			  "lottery games.")
		print("Please wait.  Depending on your inputs, it may take a while.")

		while True:
			while len(drawingresult) != self.ticketnumber:
				drawing = randint(self.lownumber, self.highnumber)
				if drawing not in drawingresult:
					drawingresult.append(drawing)
				else:
					continue

			if all(item in drawingresult for item in self.ticket):
				print("\nWe got a match!")
				print(f"Your ticket: {self.ticket}")
				print(f"Matching draws: {drawingresult}")
				repeatdrawing += 1
				print(f"It took {repeatdrawing} drawings to get a match.\n")
				break
			else:
				loopcount = 0 
				drawingresult = []
				repeatdrawing += 1
				continue

lottery = Lottery()
lottery.build_ticket()
lottery.drawings()