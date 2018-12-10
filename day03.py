def main():

	with open('inputs/day03.txt') as f:
		inputs = f.read().splitlines()

	claimed = set()
	overclaimed = set()

	claims = {}

	for row in inputs:
		
		ID = row.split(' ')[0]
		# overlap[ID] = False

		claims[ID] = set()

		start = (int(row.split(' ')[2].split(',')[0]), int(row.split(' ')[2].split(',')[1][:-1]))
		extent = (int(row.split(' ')[3].split('x')[0]), int(row.split(' ')[3].split('x')[1]))
		
		for i in range(start[0],start[0] + extent[0]):
			for j in range(start[1],start[1] + extent[1]):
				claims[ID].add((i,j))
				if (i,j) in claimed:
					overclaimed.add((i,j))
					# overlap[ID] = True
					# overlap[claimed[(i,j)]] = True
				else:
					claimed.add((i,j))
					# claimed[(i,j)] = ID

	## first answer
	print(len(overclaimed))

	## second answer
	
	for claim in claims:
		chk = claims.copy()
		del chk[claim]
		for c in chk:
			if len(claims[c] & claims[claim]) > 1:
				break
		else:
			print(claim)
			break


if __name__ == '__main__':
	main()