def qsort(arr, f):
	if (len(arr) < 2):
		return (arr,len(arr))

	pivot_index = f(arr)
	arr[pivot_index], arr[0] = arr[0], arr[pivot_index]

	i = 1
	j = 1
	while (j < len(arr)):
		if (arr[j] < arr[0]):
			arr[j],arr[i] = arr[i],arr[j]
			i = i + 1
		j = j + 1
	arr[0],arr[i-1] = arr[i-1],arr[0]
	lsorted,lcnt = qsort(arr[0:i-1], f)
	rsorted,rcnt = qsort(arr[i:len(arr)], f) 
	rescnt = lcnt + rcnt + len(arr)
	return (lsorted+[arr[i-1]]+rsorted, rescnt)

def get_index_of_el(arr,el):
	for ind, i in enumerate(arr):
		if (el == i):
			return ind

#works only on array with all distinct elements
def get_median(arr):
	first = arr[0]
	last = arr[len(arr)-1]
	med = len(arr)/2
	if len(arr)%2 == 0:
		med -= 1
	med = arr[med]
	if (first > med and med > last) or (last > med  and med > first):
		return get_index_of_el(arr,med)
	if (med > first and first > last) or (last > first and first > med):
		return get_index_of_el(arr,first)
	return get_index_of_el(arr,last)



fo = open("hw2.txt", "r")
lines = fo.readlines()
arr = []
for i in lines:
	arr.append(int(i))


# print qsort(arr, lambda arr: 0)[1] - len(arr)
# print qsort(arr, lambda arr: len(arr)-1)[1] - len(arr)
# print qsort(arr, lambda arr: get_median(arr))[1] - len(arr)

