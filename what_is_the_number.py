#!usr/bin/python3

#import modules
import random
import sys
from os import system, name

print(name)

if name == "nt":
	clear = system("cls")
else:
	clear = system("clear")

#create a random number between 1 - 10
created_number = random.randint(1,10)

chances_counter = 0
#start the loop
while True:
	#user make a guess
	print("Guess the number! (1-10) \nInput your number please: ")
	guessed_number = int(input())
	
	#Logic
	if guessed_number == created_number:
		if name == "nt":
			clear = system("cls")
		else:
			clear = system("clear")
		print("Well played! \nYou've guessed it right!")
		sys.exit()
	elif guessed_number > created_number:
		if name == "nt":
			clear = system("cls")
		else:
			clear = system("clear")
		print("Too high! \nSlow down a little bit.")
	else:
		if name == "nt":
			clear = system("cls")
		else:
			clear = system("clear")
		print("Too low! \nMake it higher.")
	
	chances_counter = chances_counter + 1	
	#It's a game over after fifth trials.
	if chances_counter == 5:
		if name == "nt":
			clear = system("cls")
		else:
			clear = system("clear")
		print("You're out of chances. \nTry your luck next time!")
		sys.exit()