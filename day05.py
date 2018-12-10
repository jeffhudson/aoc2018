import string

def main():

	with open('inputs/day05.txt') as f:
		inp = f.read()

	polymer = inp

	print len(react(polymer))

	## 2

	min_poly = (None,9999)
	for char in string.ascii_lowercase:
		tst = polymer[:]
		stripped_tst = tst.replace(char,"").replace(char.upper(),"")
		reacted = react(stripped_tst)
		if len(reacted) < min_poly[1]:
			min_poly = (char,len(reacted))
	print min_poly

def react(polymer):

	pntr = 0
	while pntr <= len(polymer) - 2:
		if polymer[pntr].lower() == polymer[pntr + 1].lower() and polymer[pntr] != polymer[pntr + 1]:
			polymer = polymer[:pntr] + polymer[pntr+2:]
			pntr = pntr - 1 if pntr > 0 else 0
		else:
			pntr += 1

	return polymer

if __name__ == '__main__':
	main()