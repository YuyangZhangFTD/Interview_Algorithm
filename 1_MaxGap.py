"""
    max gap 
    input:  [2.3, 3.1, 7.5, 1.5, 6.3]
    output: 3.2 
"""
import math
X = [2.3, 3.1, 7.5, 1.5, 6.3]
min_x = min(X)
max_x = max(X)
n = len(X)
low = [max_x for i in range(n+1)]
high = [min_x for i in range(n+1)]
count = [0 for i in range(n+1)]
for i in range(n):
	bucket = math.floor((n-1)*(X[i]-min_x)/(max_x-min_x))+1
	count[bucket] += 1
	if X[i] < low[bucket]:
		low[bucket] = X[i]
	if X[i] > high[bucket]:
		high[bucket] = X[i]
tmp = 0
left = high[1]
for i in range(2,n):
	if count[i] > 0:
		gap = low[i] - left
		if gap > tmp:
			tmp = gap
		left = high[i]
print(gap)
