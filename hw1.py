def msort_inv(arr):
	if (len(arr) < 2):
		return (arr,0)
	if (len(arr) == 2):
		cnt = 0
		if (arr[0] > arr[1]):
			tmp = arr[0]
			arr[0] = arr[1]
			arr[1] = tmp
			cnt = 1
		return (arr,cnt)

	mid = len(arr) / 2
	left = arr[0:mid]
	right = arr[mid:len(arr)]
	leftsorted, leftcnt = msort_inv(left) 
	rightsorted, rightcnt = msort_inv(right)
	splitscnt = 0
	res = []
	li = 0
	ri = 0
	while (li < len(leftsorted) and ri < len(rightsorted)):
		if (leftsorted[li] < rightsorted[ri]):
			res.append(leftsorted[li])
			li = li + 1
		else:
			res.append(rightsorted[ri])
			ri = ri + 1
			splitscnt = splitscnt + len(leftsorted) - li
	if (li < len(leftsorted)):
		for k in range(li, len(leftsorted)):
			res.append(leftsorted[k])
	if (ri < len(rightsorted)):
		for k in range(ri, len(rightsorted)):
			res.append(rightsorted[k])
	return (res,splitscnt+leftcnt+rightcnt)


# print msort_inv([6,5,4,3,2,1])
fo = open("hw1.txt", "r")
lines = fo.readlines()
arr = []
for i in lines:
	arr.append(int(i))

print msort_inv(arr)[1]
