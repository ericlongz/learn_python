#!/usr/bin/python3

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
	#Code that creates a list of 100 'heads' or 'tails' values.
	ht_list = []
	streak = 0
	for i in range(100):
		ht_list.append(random.randint(0,1))

	#Code that checks if there is a streak of 6 heads or tails in a row.
		if i == 0:
			pass
		else:
			if ht_list[i] == ht_list[i-1]:
				streak = streak + 1
			else:
				streak = 0
		
		if streak == 6:
			numberOfStreaks += 1
			break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

