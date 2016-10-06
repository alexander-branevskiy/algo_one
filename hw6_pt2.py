import heapq

#copied from http://stackoverflow.com/questions/407734/a-generic-priority-queue-for-python
class PriorityQueueSet(object):

    """
    Combined priority queue and set data structure.

    Acts like a priority queue, except that its items are guaranteed to be
    unique. Provides O(1) membership test, O(log N) insertion and O(log N)
    removal of the smallest item.

    Important: the items of this data structure must be both comparable and
    hashable (i.e. must implement __cmp__ and __hash__). This is true of
    Python's built-in objects, but you should implement those methods if you
    want to use the data structure for custom objects.
    """

    def __init__(self, items=[]):
        """
        Create a new PriorityQueueSet.

        Arguments:
            items (list): An initial item list - it can be unsorted and
                non-unique. The data structure will be created in O(N).
        """
        self.set = dict((item, True) for item in items)
        self.heap = self.set.keys()
        heapq.heapify(self.heap)

    def has_item(self, item):
        """Check if ``item`` exists in the queue."""
        return item in self.set

    def pop_smallest(self):
        """Remove and return the smallest item from the queue."""
        smallest = heapq.heappop(self.heap)
        del self.set[smallest]
        return smallest

    def add(self, item):
        """Add ``item`` to the queue if doesn't already exist."""
        if item not in self.set:
            self.set[item] = True
            heapq.heappush(self.heap, item)

    def size(self):
    	return len(self.heap)        




class El(object):
	def __init__(self, val, priority):
		self.priority = priority
		self.val = val
	def __cmp__(self, other):
		return cmp(self.priority, other.priority)


# pq = PriorityQueueSet()
# pq.add(El(1,2))
# pq.add(El(2,3))
# print pq.pop_smallest().val

fo = open("hw6_2.txt", "r")
lines = fo.readlines()

# def debug(pq):
# 	size = pq.size()
# 	mem = [] 
# 	while pq.size() > 0:
# 		mem.append(pq.pop_smallest());
# 	toprint = []
# 	for i in mem:
# 		toprint.append(i.val)
# 		pq.add(i)

# 	assert(pq.size()==size)
# 	return toprint

pq_min = PriorityQueueSet()
pq_max = PriorityQueueSet()

first = int(lines[0])
del lines[0]
# print first
second = int(lines[0])
del lines[0]
# print first

ans = first
if second > first:
	ans += first
else:
	ans += second

if first < second:
    pq_max.add(El(first, -first))
    pq_min.add(El(second, second))
else:
    pq_max.add(El(second, -second))
    pq_min.add(El(first, first))

for i in lines:
	next = int(i)
	mx = pq_max.pop_smallest()
	if next < mx.val:
		pq_max.add(El(next, -next))
	else:
		pq_min.add(El(next, next))
	pq_max.add(mx)

	if pq_max.size() - pq_min.size() >= 2:
		e = pq_max.pop_smallest()
		e.priority = -e.priority
		pq_min.add(e)
	if pq_min.size() - pq_max.size() >= 2:
		e = pq_min.pop_smallest()
		e.priority = -e.priority
		pq_max.add(e)

	# print debug(pq_max), debug(pq_min)
	if pq_max.size() > pq_min.size():
		e = pq_max.pop_smallest()
		ans += e.val
		# print e.val, "max>min\n"
		pq_max.add(e)
	elif pq_max.size() < pq_min.size():
		e = pq_min.pop_smallest()
		ans += e.val
		pq_min.add(e)
		# print e.val, "max<min\n"
	else:
		e = pq_max.pop_smallest()
		ans += e.val
		pq_max.add(e)
		# print e.val, "=\n"

print ans%10000


