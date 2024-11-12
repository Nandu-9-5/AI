import random
def choice():
	ch = input('Do you want to play first:')
	if ch.lower().startswith('y'):
		return [3,5]
	return [5,3]

def isEmpty(board, i):
	if board[i]==2:
		return True;
	return False

def chooseRandom(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isEmpty(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def makeMove(b, player, pos):
	b[pos]=player

def isWinner(b, p):
	if b[1]==b[2]==b[3]==p:
		return True
	if b[4]==b[5]==b[6]==p:
		return True
	if b[7]==b[8]==b[9]==p:
		return True
	if b[1]==b[4]==b[7]==p:
		return True
	if b[2]==b[5]==b[8]==p:
		return True
	if b[3]==b[6]==b[9]==p:
		return True
	if b[1]==b[5]==b[9]==p:
		return True
	if b[3]==b[5]==b[7]==p:
		return True
	return False

def hmove(h):
	pos=int(input('Enter pos: '))
	if isEmpty(board,pos):
		return pos
	return hmove(h)

def cmove(h, c, b):
	for i in range(1,10):
		cpy = b.copy()
		if isEmpty(board,i):
		    makeMove(cpy, c, i)
		    if isWinner(cpy, c):
		    	return i
	for i in range(1,10):
		cpy = b.copy()
		if isEmpty(board,i):
		    makeMove(cpy, h, i)
		    if isWinner(cpy, h):
		    	return i
	move = chooseRandom(board, [1, 3, 7, 9])
	if move != None:
		return move
	if isEmpty(board, 5):
		return 5
	return chooseRandom(board, [2, 4, 6, 8])

def draw(b):
	for i in range(1, 10):
		if i in [3,6,9]:
			if b[i]==3:
				print('X')
			elif b[i]==5:
				print('O')
			else:
				print('-')
		else:
			if b[i]==3:
				print('X', end=' ')
			elif b[i]==5:
				print('O', end=' ')
			else:
				print('-', end=' ')


print('Welcome to the game')
i=-1
board = [2] * 10
h,c = choice()
player = (h,c)[h>c]
turn=0
for turn in range(1, 10):
	if player==h:
		move = hmove(h)
		makeMove(board, player, move)
		draw(board)
		print()
		if isWinner(board, player):
			print('You won')
			break
		player=c
	else:
		move = cmove(h, c, board)
		makeMove(board, player, move)
		draw(board)
		if isWinner(board, player):
			print('You lose')
			break
		player=h
if turn>=9:
    print('The game is tie!')
