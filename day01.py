
def main():
	with open('inputs/day01.txt') as f:
		thingy = f.read().splitlines()

	
	counter = 0
	for row in thingy:
		if row[0] == '+':
			counter += int(row[1:])
		else:
			counter -= int(row[1:])

	print(' '.join(["first answer is:",str(counter)]))


	freqs = set([0])
	found = False
	counter = 0
	while not found:
		for row in thingy:
			if row[0] == '+':
				counter += int(row[1:])
			else:
				counter -= int(row[1:])
			if counter in freqs:
				found = True
				print(' '.join(["second answer is:", str(counter)]))
				break
			else:
				freqs.add(counter)

if __name__ == '__main__':
	main()