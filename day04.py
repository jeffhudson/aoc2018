def main():

	with open('inputs/day04.txt') as f:
		inputs = f.read().splitlines()


	ordered = []
	for row in inputs:
		ID = row.split(']')[0][1:]
		statement = row.split(']')[1][1:]
		ordered.append((ID,statement))

	ordered.sort(key=lambda x: x[0])

	active_guard = None
	sleep_start  = None
	summary = {}
	for time, obs in ordered:
		if obs[0] == 'G':
			active_guard = obs.split(' ')[1]
			if active_guard not in summary.keys():
				summary[active_guard] = {}
				summary[active_guard]['total_slept'] = 0
				summary[active_guard]['minutes_count'] = {}
				for i in range(0,60):
					summary[active_guard]['minutes_count'][i] = 0
		elif obs[0] == 'f':
			sleep_start = int(time.split(' ')[1].split(':')[1])
		elif obs[0] == 'w':
			sleep_end = int(time.split(' ')[1].split(':')[1])
			summary[active_guard]['total_slept'] +=  sleep_end - sleep_start
			for i in range(sleep_start,sleep_end):
				summary[active_guard]['minutes_count'][i] += 1

	sleepiest_guard = (None, 0)
	for guard in summary:
		if summary[guard]['total_slept'] > sleepiest_guard[1]:
			sleepiest_guard = (guard,summary[guard]['total_slept'])

	sleepiest_minute = (None, 0)
	for i in summary[sleepiest_guard[0]]['minutes_count']:
		if summary[sleepiest_guard[0]]['minutes_count'][i] > sleepiest_minute[1]:
			sleepiest_minute = (i, summary[sleepiest_guard[0]]['minutes_count'][i])

	print(sleepiest_guard, sleepiest_minute)
	print(int(sleepiest_guard[0][1:]) * sleepiest_minute[0])

	sleepiest_minute_2 = (None, None, 0)
	for guard in summary:
		for i in summary[guard]['minutes_count']:
			if summary[guard]['minutes_count'][i] > sleepiest_minute_2[2]:
				sleepiest_minute_2 = (int(guard[1:]),i,summary[guard]['minutes_count'][i])

	print sleepiest_minute_2, sleepiest_minute_2[0] * sleepiest_minute_2[1]

if __name__ == '__main__':
	main()