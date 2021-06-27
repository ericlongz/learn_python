#!/usr/bin/python3

#import modules
import random
import copy
import time

#set the width and height of the field
width = 60
height = 20

#create initial condition of the field
nextcells = []
for i in range(height):
	list_column = []
	for j in range(width):
		value = random.randint(0,1)
		if value == 0:
			list_column.append("*")
		else:
			list_column.append(" ")
	nextcells.append(list_column)

#counter_saved_cells = 0

#start loop
while True:
	#set how many step so we can save the cells
	#save_step = 3
	
	print("\n\n\n\n\n\n\n\n")
	#print current cells
	current_cells = copy.deepcopy(nextcells)
	for x in range(height):
		for y in range(width):
			print(current_cells[x][y], end="")
		print()
		
	#create next cells
	for x in range(height):
		for y in range(width):
			counter = 0
			top = " "
			bottom = " "
			right = " "
			toprig = " "
			botrig = " "
			left = " "
			topleft = " "
			botleft = " "
			
			if x == 0:
				if y == 0:
					bottom = current_cells[x+1][y+0]
					right = current_cells[x+0][y+1]
					botrig = current_cells[x+1][y+1]
				elif y == (width-1):
					bottom = current_cells[x+1][y+0]
					left = current_cells[x+0][y-1]
					botlef = current_cells[x+1][y-1]
				else:
					bottom = current_cells[x+1][y+0]
					right = current_cells[x+0][y+1]
					botrig = current_cells[x+1][y+1]
					left = current_cells[x+0][y-1]
					botlef = current_cells[x+1][y-1]
			elif x == (height-1):
				if y == 0:
					top = current_cells[x-1][y+0]
					right = current_cells[x+0][y+1]
					toprig = current_cells[x-1][y+1]
				elif y == (width-1):
					top = current_cells[x-1][y+0]
					left = current_cells[x+0][y-1]
					toplef = current_cells[x-1][y-1]
				else:
					top = current_cells[x-1][y+0]
					right = current_cells[x+0][y+1]
					toprig = current_cells[x-1][y+1]
					left = current_cells[x+0][y-1]
					toplef = current_cells[x-1][y-1]
			else:
				if y == 0:
					top = current_cells[x-1][y+0]
					bottom = current_cells[x+1][y+0]
					right = current_cells[x+0][y+1]
					toprig = current_cells[x-1][y+1]
					botrig = current_cells[x+1][y+1]
				elif y == (width-1):
					top = current_cells[x-1][y+0]
					bottom = current_cells[x+1][y+0]
					left = current_cells[x+0][y-1]
					toplef = current_cells[x-1][y-1]
					botleft = current_cells[x+1][y-1]
				else:
					top = current_cells[x-1][y+0]
					bottom = current_cells[x+1][y+0]
					right = current_cells[x+0][y+1]
					toprig = current_cells[x-1][y+1]
					botrig = current_cells[x+1][y+1]
					left = current_cells[x+0][y-1]
					toplef = current_cells[x-1][y-1]
					botleft = current_cells[x+1][y-1]
			
			#count counters
			if top == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if bottom == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if right == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if toprig == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if botrig == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if left == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if topleft == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			if botleft == "*":
				counter = counter + 1
			else:
				counter = counter + 0
			
			#Conway's Rules:
			if current_cells[x][y] == "*":
				if (counter == 2) or (counter == 3):
					nextcells[x][y] = "*"
				else:
					nextcells[x][y] = " "
			else:
				if counter == 3:
					nextcells[x][y] = "*"
				else:
					nextcells[x][y] = " "
				
	#if (counter_saved_cells != 0) and (counter_saved_cells % save_step == 0):
	#	for x in range(height):
	#		for y in range(width):
	#			if (saved_cells[x][y] == " ") and (nextcells[x][y] == " "):
	#				nextcells[x][y] = "#"
		
	#if (counter_saved_cells % save_step) == 0:
	#	saved_cells = copy.deepcopy(nextcells)
		
	#counter_saved_cells = counter_saved_cells + 1
	time.sleep(1)
	