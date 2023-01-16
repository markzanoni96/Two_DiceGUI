"""
1/10/2023  Program: TwoDiceGUI.py

Chapter 8 example demostrating the use of file dialogs with a GUI


NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# other imports can go here

class TwoDiceGUI(EasyFrame):
	

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Two Dice Game", width = 340, height = 280, resizable = False, background = "seagreen")
		self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "seagreen", foreground = "white", font = Font(family = "Impact", size = 26))
		self.addLabel(text = "Player's Roll:", row = 1, column = 0, background = "seagreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, columnspan = 2, width = 10, state = "readonly")
		self.addLabel(text = "Computer's Roll:", row = 2, column = 0, background = "seagreen")
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, width = 10, state = "readonly")

		
		self.addButton(text = "Roll Dice!", row = 3, column = 0, columnspan = 2, command = self.roll)
		self.resultArea = self.addLabel(text = "You Have Won!", row = 4, column = 0, columnspan = 2, sticky = "NSEW", background = "seagreen", foreground = "white", font = Font(family = "Georgia", size = 22))

	# definition of the self.roll() function which handles the event
	def roll(self):
		# variables for the function
		die1 = random.randint(1, 6)
		die2 = random.randint(1, 6)

		# processing phase
		if die1 > die2:
			result = "You Win!"
			self.resultArea["foreground"] = "yellow"
		elif die1 < die2:
			result = "You lose!"
			self.resultArea["foreground"] = "red"
		else:
			result = "We have a tie!"
			self.resultArea["foreground"] = "white"

		# output phase
		self.playerRoll.setNumber(die1)
		self.computerRoll.setNumber(die2)
		self.resultArea["text"] = result	





# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	TwoDiceGUI().mainloop()

# global call to the main() method
main()


