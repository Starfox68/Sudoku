def solve(bo):
	find = find_empty(bo)
	if not find:
		return True
	else:
		row, col = find

	for i in range(1, 10):
		if valid(bo, i, (row,col)):
			bo[row][col] = i

			if (solve(bo)):
				return True

			bo[row][col] = 0

	return False


def valid(bo, num, pos):
	row = pos[0]
	col = pos[1]

	#check row
	for i in range(len(bo)):
		if (bo[row][i] == num and col != i):
			return False

	#check column
	for i in range(len(bo)):
		if (bo[i][col] == num and row != i):
			return False

	#check square
	box_x = col // 3
	box_y = row // 3

	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if (bo[i][j] == num and (i,j) != pos):
				return False

	return True

def print_board(bo):
	for i in range(len(bo)):
		for j in range(len(bo)):
			if (j % 3 == 0 and j != 0):
				print("| " + str(bo[i][j]) + " ", end = '')
			elif (j == (len(bo)-1)):
				print(str(bo[i][j]))
			else:
				print(str(bo[i][j]) + " ", end = '')

		if ((i+1) % 3 == 0):
			print("- - - - - - - - - - -")


def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo)):
			if (bo[i][j] == 0):
				return (i, j) #row then column

	return False
	