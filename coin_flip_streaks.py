#!/usr/bin/python3

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
	#Code that creates a list of 100 'heads' or 'tails' values.
	headTail = ""
	for i in range(100):
		headTail = headTail + str(random.randint(0,1))

	#Code that checks if there is a streak of 6 heads or tails in a row.
	if ('000000' in headTail) or ('111111' in headTail):
		numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

