#!/usr/bin/python3

#import modules
import random
import copy
import time

#set the width and height of the field
width = 60
height = 20

#create initial condition of the field
list_row = []
for i in range(height):
	list_column = []
	for j in range(width):
		value = random.randint(0,1)
		if value == 0:
			list_column.append(" ")
		else:
			list_column.append("#")
			