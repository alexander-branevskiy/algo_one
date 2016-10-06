fo = open("hw6.txt", "r")
lines = fo.readlines()

ht = set([])
tot = []

for i in lines:
	casted = int(i)
	if not casted in ht:
		ht.add(casted)
		tot.append(casted)


ans = 0
for t in range(-10000, 10001):
	print t
	for first in tot:
		if (t - first) in ht:
			ans += 1

print ans