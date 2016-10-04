import random
import math

#copied from http://www.ics.uci.edu/~eppstein/PADS/UnionFind.py
class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

# dsu = UnionFind()
# dsu.union(1,2)
# print dsu[1]
# print dsu[2]
# print dsu[3]

def getKargerMinCut(edges, totvertexes):
    dsu = UnionFind()
    offset = 0
    maxoffset = len(edges) - 1
    while totvertexes > 2:
        ind = random.randint(offset, maxoffset)
        e = edges[ind]
        v1 = e[0]
        v2 = e[1]
        anc1 = dsu[v1]
        anc2 = dsu[v2]
        if (anc1 == anc2):
            dsu.union(v1,v2)
        else:
            dsu.union(v1,v2)
            totvertexes -= 1

        edges[ind], edges[offset] = edges[offset], edges[ind]
        offset += 1

    ans = 0
    for e in edges:
        anc1 = dsu[e[0]]
        anc2 = dsu[e[1]]
        if anc1 != anc2:
            ans += 1

    return ans

######read input
fo = open("hw3.txt", "r")
lines = fo.readlines()
totvertexes = len(lines)
edges = []
for i in lines:
    splits = i.split('\t')
    del splits[-1]
    _from = int(splits[0])
    del splits[0]
    for to in splits:
        casted_to = int(to)
        if _from < casted_to:
            edges.append((_from,casted_to))

#########run karger n*n*(log(n)+1) times
maxit = int((math.log(totvertexes,2)+1) * totvertexes * totvertexes)
best = 2282281488
for i in range(0, maxit):
    cur = getKargerMinCut(edges, totvertexes)
    if cur < best:
        best = cur

    if i%1000 == 0:
        print "current iteration = ", i
        print "current best = ", best
        print "iteration remains = ", maxit - i
        print "\n\n"

print best
