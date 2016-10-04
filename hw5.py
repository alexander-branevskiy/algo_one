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




class VertexWithPrior(object):
	def __init__(self, priority, vertex):
		self.priority = priority
		self.vertex = vertex
	def __cmp__(self, other):
		return cmp(self.priority, other.priority)

# pq = PriorityQueueSet()
# pq.add(VertexWithPrior(228,1))
# pq.add(VertexWithPrior(227,2))
# pq.add(VertexWithPrior(1488,3))
# print pq.pop_smallest().vertex
# print pq.size()

totvertexes = 200
adj = [[0 for i in range(totvertexes)] for j in range(totvertexes)]

fo = open("hw5.txt", "r")
lines = fo.readlines()
for i in lines:
	splits = i.split("\t")
	del splits[-1]
	_from = int(splits[0]) - 1
	del splits[0]
	for j in splits:
		vertex_and_w = j.split(",")
		to = int(vertex_and_w[0]) - 1
		w = int(vertex_and_w[1])
		adj[_from][to] = w

# print adj

def getDijkstraShortestPath(source):
	global adj, totvertexes

	used = [False] * totvertexes
	weights = [2282281488] * totvertexes
	weights[source] = 0

	pq = PriorityQueueSet()
	pq.add(VertexWithPrior(0,source))

	while pq.size() > 0:
		_from = pq.pop_smallest().vertex
		if not used[_from]:
			for to in range(0, totvertexes):
				if not used[to] and adj[_from][to] > 0:
					if adj[_from][to] + weights[_from] < weights[to]:
						weights[to] = adj[_from][to] + weights[_from]
						pq.add(VertexWithPrior(weights[to], to))

		used[_from] = True
	return weights

ans = getDijkstraShortestPath(0)

# 7,37,59,82,99,115,133,165,188,197

#-1 here because vertexes labeled like [0 .. vertex - 1]
print ans[6],ans[36],ans[58],ans[81],ans[98],ans[114],ans[132],ans[164],ans[187],ans[196]