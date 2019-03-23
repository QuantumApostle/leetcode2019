# LC 684

class UnionFindSet:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1 for i in range(size + 1)]

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent:
            return False
        if self.rank[p_parent] > self.rank[q_parent]:
            self.parent[q_parent] = p_parent
        elif self.rank[p_parent] < self.rank[q_parent]:
            self.parent[p_parent] = q_parent
        else:
            self.parent[p_parent] = q_parent
            self.rank[q_parent] += 1
        return True


class Solution:

    def findRedundantConnection(self, edges):
        uf = UnionFindSet(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        return None


if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(Solution().findRedundantConnection(edges))
