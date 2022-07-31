for _ in range(int(input())):
	n = int(input())
	a = sorted(list(map(int, input().split())))
	freq = [0]*1001
	for x in a:
		freq[x] += 1
	ans = 0
	for d in range(1, 1001):
		cur = 0
		mark = [0]*1001
		for x in a:
			if mark[x] == 1:
				continue
			ptr = x
			tot = 0
			mx = 0
			while ptr <= 1000:
				if freq[ptr] == 0:
					break
				mark[ptr] = 1
				tot += freq[ptr]
				mx = max(mx, freq[ptr])
				ptr += d
			if mx > 1 or tot%2 == 0:
				cur += tot
			else:
			    cur += tot-1
		ans = max(ans, cur)
	print(ans)