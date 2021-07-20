print("Let's Play TicTacToe.")
print("Move's info: \nTL= Top Left \tTM= Top Mid \tTR= Top Right \nML= Mid Left \tMM = Center \tMR= Mid Right \nLL= Low Left \tLM= Low Mid \tLR= Low Right")

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	
def playerOneMove():
	print("Player 1's Move (X). \nInput your move(TL, TM, TR, ML, MM, MR, LL, LM, LR):")
	
playerOneMove()