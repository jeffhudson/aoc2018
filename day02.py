def main():

	with open('inputs/day02.txt') as f:
		thingy = f.read().splitlines()

	x2s = 0
	x3s = 0
	for row in thingy:
		for r in row:
			if row.count(r) == 2:
				x2s += 1
				break
		for r in row:
			if row.count(r) == 3:
				x3s += 1
				break

	print(' '.join(["first answer is:",str(x2s * x3s)]))
		

	# chk = thingy.copy()
	found = False
	while not found:
		chk = thingy.pop()
		for row in thingy:
			res = edit_distance(chk,row)
			if res[0] == 1:
				found = True
				break

	print(' '.join(["second answer is:",res[1]]))

def edit_distance(chk,row):

	dist = 0
	sames = ''
	for i in range(0,len(chk)):
		if chk[i] != row[i]:
			dist += 1
		else:
			sames += chk[i]

	return dist, sames


if __name__ == '__main__':
	main()