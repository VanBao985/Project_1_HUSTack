# Minimum Spanning Tree - Kruskal
# Given a undirected connected graph G=(V,E) where V={1,…,N}. 
# Each edge (u,v)∈E(u,v)∈E has weight w(u,v)w(u,v). Compute minimum spanning tree of G.

# Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(0, n))  
        self.rank = [0] * n   # the depth of the tree rooted at i
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    mst = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += w
    return mst

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

edges.sort(key=lambda x: x[2])  # sort by weight
print(kruskal(n, edges))