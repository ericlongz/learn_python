#!/usr/bin/python3

def main():
	global theBoard
	
	print("Let's Play TicTacToe.")
	print("Move's info: \nTL= Top Left \tTM= Top Mid \tTR= Top Right \nML= Mid Left \tMM = Center \tMR= Mid Right \nLL= Low Left \tLM= Low Mid \tLR= Low Right")

	theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
	while True:
		printBoard(theBoard)
		playerOneMove()
		game_logic()
		printBoard(theBoard)
		playerTwoMove()
		game_logic()
	
def game_logic():
	import sys
	top_values = 0
	mid_values = 0
	low_values = 0
	left_values = 0
	middle_values = 0
	right_values = 0
	tl_to_lr_diag_values = 0
	tr_to_ll_diag_values = 0
	all_values = 0
	for i in theBoard.keys():
		if 'top' in i:
			if '-L' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					top_values = top_values + 1
					left_values = left_values + 1
					tl_to_lr_diag_values = tl_to_lr_diag_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					top_values = top_values - 1
					left_values = left_values - 1
					tl_to_lr_diag_values = tl_to_lr_diag_values - 1
			elif '-M' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					top_values = top_values + 1
					middle_values = middle_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					top_values = top_values - 1
					middle_values = middle_values - 1
			elif '-R' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					top_values = top_values + 1
					right_values = right_values + 1
					tr_to_ll_diag_values = tr_to_ll_diag_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					top_values = top_values - 1
					right_values = right_values - 1
					tr_to_ll_diag_values = tr_to_ll_diag_values - 1
		elif 'mid' in i:
			if '-L' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					mid_values = mid_values + 1
					left_values = left_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					mid_values = mid_values - 1
					left_values = left_values - 1
			elif '-M' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					mid_values = mid_values + 1
					middle_values = middle_values + 1
					tl_to_lr_diag_values = tl_to_lr_diag_values + 1
					tr_to_ll_diag_values = tr_to_ll_diag_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					mid_values = mid_values - 1
					middle_values = middle_values - 1
					tl_to_lr_diag_values = tl_to_lr_diag_values - 1
					tr_to_ll_diag_values = tr_to_ll_diag_values - 1
			elif '-R' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					mid_values = mid_values + 1
					right_values = right_values + 1
				if theBoard[i] == "O":
					all_values = all_values + 1
					mid_values = mid_values - 1
					right_values = right_values - 1
		elif 'low' in i:
			if '-L' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					low_values = low_values + 1
					left_values = left_values + 1
					tr_to_ll_diag_values = tr_to_ll_diag_values + 1
				if theBoard[i] == "O":
					all_values = all_values + 1
					low_values = low_values - 1
					left_values = left_values - 1
					tr_to_ll_diag_values = tr_to_ll_diag_values - 1
			elif '-M' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					low_values = low_values + 1
					middle_values = middle_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					low_values = low_values - 1
					middle_values = middle_values - 1
			elif '-R' in i:
				if theBoard[i] == "X":
					all_values = all_values + 1
					low_values = low_values + 1
					right_values = right_values + 1
					tl_to_lr_diag_values = tl_to_lr_diag_values + 1
				elif theBoard[i] == "O":
					all_values = all_values + 1
					low_values = low_values - 1
					right_values = right_values - 1
					tl_to_lr_diag_values = tl_to_lr_diag_values - 1
	
	if (top_values == 3) or (mid_values == 3) or (low_values == 3) or (left_values == 3) or (middle_values == 3) or (right_values == 3) or (tl_to_lr_diag_values == 3) or (tr_to_ll_diag_values == 3):
		printBoard(theBoard)
		print("Congratulation! Player 1 Win.")
		sys.exit()
	elif (top_values == -3) or (mid_values == -3) or (low_values == -3) or (left_values == -3) or (middle_values == -3) or (right_values == -3) or (tl_to_lr_diag_values == -3) or (tr_to_ll_diag_values == -3):
		printBoard(theBoard)
		print("Congratulation! Player 2 Win.")
		sys.exit()
	elif all_values == 9:
		printBoard(theBoard)
		print("It's a Draw.")
		sys.exit()	

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	
def playerOneMove():
	print("Player 1's Move (X). \nInput your move(TL, TM, TR, ML, MM, MR, LL, LM, LR):")
	move_input = str(input())
	if move_input.lower() == 'tl':
		if theBoard['top-L'] == ' ':
			theBoard['top-L'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'tm':
		if theBoard['top-M'] == ' ':
			theBoard['top-M'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'tr':
		if theBoard['top-R'] == ' ':
			theBoard['top-R'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'ml':
		if theBoard['mid-L'] == ' ':
			theBoard['mid-L'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'mm':
		if theBoard['mid-M'] == ' ':
			theBoard['mid-M'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'mr':
		if theBoard['mid-R'] == ' ':
			theBoard['mid-R'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'll':
		if theBoard['low-L'] == ' ':
			theBoard['low-L'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'lm':
		if theBoard['low-M'] == ' ':
			theBoard['low-M'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	elif move_input.lower() == 'lr':
		if theBoard['low-R'] == ' ':
			theBoard['low-R'] = 'X'
		else:
			print("Please take another move! This one is taken.")
			playerOneMove()
	else:
		print("Please input the right move!")
		playerOneMove()
		
def playerTwoMove():
	print("Player 2's Move (O). \nInput your move(TL, TM, TR, ML, MM, MR, LL, LM, LR):")
	move_input = str(input())
	if move_input.lower() == 'tl':
		if theBoard['top-L'] == ' ':
			theBoard['top-L'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'tm':
		if theBoard['top-M'] == ' ':
			theBoard['top-M'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'tr':
		if theBoard['top-R'] == ' ':
			theBoard['top-R'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'ml':
		if theBoard['mid-L'] == ' ':
			theBoard['mid-L'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'mm':
		if theBoard['mid-M'] == ' ':
			theBoard['mid-M'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'mr':
		if theBoard['mid-R'] == ' ':
			theBoard['mid-R'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'll':
		if theBoard['low-L'] == ' ':
			theBoard['low-L'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'lm':
		if theBoard['low-M'] == ' ':
			theBoard['low-M'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	elif move_input.lower() == 'lr':
		if theBoard['low-R'] == ' ':
			theBoard['low-R'] = 'O'
		else:
			print("Please take another move! This one is taken.")
			playerTwoMove()
	else:
		print("Please input the right move!")
		playerTwoMove()
	

main()