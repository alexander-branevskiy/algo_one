import itertools
import resource, sys, threading
###redundant vertexes will be just single strong component
maxvertexes = 1000000

gr = []
grrev = [] 
for i in range(0, maxvertexes):
	gr.append([])
	grrev.append([])

used = [False] * maxvertexes
backorder = []

def main():
	def setFalse(arr):
		arr[:] = itertools.repeat(False, len(arr))

	def dfs1(v):
		global used, gr, backorder
		used[v] = True
		for out in gr[v]:
			if not used[out]:
				dfs1(out)
		backorder.append(v)

	def dfs2(v):
		global used, grrev
		used[v] = True
		cnt = 1
		for out in grrev[v]:
			if not used[out]:
				# print "from, to = ",v+1,out+1, grrev[v]
				cnt += dfs2(out)
		return cnt

	fo = open("hw4.txt", "r")
	lines = fo.readlines()

	for i in lines:
		splits = i.split(" ")
		del splits[-1]
		v1 = int(splits[0])
		v2 = int(splits[1])
		if v1 != v2:
			gr[v1-1].append(v2-1)
			grrev[v2-1].append(v1-1)

	for v in range(0, maxvertexes):
		if not used[v]:
			dfs1(v)

	setFalse(used)

	print "back order calculated, start output components"

	ans = []
	for v in reversed(backorder):
		if not used[v]:
			ans.append(dfs2(v))
	ans = sorted(ans)
	print ans[-1], ans[-2], ans[-3], ans[-4], ans[-5]



##hack to avoid recursion stack constraints
threading.stack_size(67108864)
sys.setrecursionlimit(maxvertexes)
thread = threading.Thread(target=main)
thread.start()