# Shortest Path between 2 nodes on a directed graph with non-negative weights
# Given a directed graph G = (V,E) in which V = {1,2,...,n) is the set of nodes. Each arc (u,v) has a 
# non-negative weight w(u,v). Given two nodes s and t of G. Find the shortest path from s to t on G.

# Djikstra's algorithm
from heapq import heappush, heappop, heapify
from collections import defaultdict
class Graph:
     def __init__(self, n):
          self.graph = defaultdict(dict)
     
     def add_node(self, u, v, w):
          if self.graph[u] is None:
               self.graph[u] = {}
          self.graph[u][v] = w
     def shortest_distance(self, source):
          distance = {node: float('inf') for node in self.graph}
          distance[source] = 0
          visited = set()

          pq = [(0, source)]
          heapify(pq)
          while pq:
               current_distance, current_node = heappop(pq)
               if current_node in visited:
                    continue
               visited.add(current_node)
               for neighbor, weight in self.graph[current_node].items():
                    new_weight = current_distance + weight  
                    if new_weight < distance[neighbor]:
                         distance[neighbor] = new_weight
                         heappush(pq, (new_weight, neighbor))
          predecessors = {node: None for node in self.graph}
          for node in self.graph:
               for neighbor, weight in self.graph[node].items():
                    if distance[node] + weight == distance[neighbor]:
                         predecessors[neighbor] = node

          return distance, predecessors

     def shortest_path(self, source, target):
          distance, predecessors = self.shortest_distance(source)
          path = []
          while target:
               path.append(target)
               target = predecessors[target]
          path.reverse()
          return distance, path

n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
     u, v, w = map(int, input().split())
     graph.add_node(u, v, w)  
source, target = map(int, input().split())
distance, path = graph.shortest_path(source, target)
print(distance[target])