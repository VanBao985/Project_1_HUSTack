class Graph:
    def __init__(self, graph, n):
        self.graph = graph
        self.n = n

    def bfs(self, source, target, parent):
        queue = [source]
        visited = [False] * self.n
        visited[source] = True
        while queue:
            node = queue.pop(0)
            if node == target:
                break
            for i in range(self.n):
                if visited[i] == False and self.graph[node][i] > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = node
        return visited[target]

    def edmonds_karp(self, source, target):
        parent = [-1] * self.n
        max_flow = 0
        
        while self.bfs(source, target, parent):
            increase = 10**9
            t = target
            while t != source:
                increase = min(increase, self.graph[parent[t]][t])
                t = parent[t]
            
            max_flow += increase
            t = target
            while t != source:
                self.graph[parent[t]][t] -= increase
                self.graph[t][parent[t]] += increase
                t = parent[t]
            
        return max_flow
    
n, m = map(int, input().split())
source, target = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w

g = Graph(graph, n)
max_flow = g.edmonds_karp(source-1, target-1)
print(max_flow)