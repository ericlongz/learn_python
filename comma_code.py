#!/usr/bin/python3

###Make a function to read everything inside a list.

def comma_code(spam):
	output = ""
	for i,j in enumerate(spam):
		if i == len(spam)-1:
			output = output + "and " + str(j)
		else:
			output = output + str(j) + " "
	return output

print("Try input a list")
print("How many value do you want to input?:")
loop_int = int(input())

#Build a list
spam = []
print("Input the value(s):")
for i in range(loop_int):
	spam.append(str(input()))

print(comma_code(spam))
