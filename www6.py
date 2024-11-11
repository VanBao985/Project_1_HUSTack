# Shortest Path between 2 nodes on a directed graph with non-negative weights
# Given a directed graph G = (V,E) in which V = {1,2,...,n) is the set of nodes. Each arc (u,v) has a 
# non-negative weight w(u,v). Given two nodes s and t of G. Find the shortest path from s to t on G.

# Djikstra's algorithm
from heapq import heappush, heappop
from collections import defaultdict
class Graph:
     def __init__(self, n):
          self.graph = defaultdict(list)
          self.n = n
     
     def add_node(self, u, v, w):
          self.graph[u].append((v, w))
     def shortest_distance(self, source, target):
          INF = 10**9
          distance = [INF ] * (self.n + 1)
          distance[source] = 0

          pq = [(0, source)]
          while pq:
               current_distance, current_node = heappop(pq)
               if current_distance > distance[current_node]:
                    continue
               if current_node == target:
                    return current_distance
               for neighbor, weight in self.graph[current_node]:
                    new_weight = current_distance + weight  
                    if new_weight < distance[neighbor]:
                         distance[neighbor] = new_weight
                         heappush(pq, (new_weight, neighbor))
          return -1


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
     u, v, w = map(int, input().split())
     graph.add_node(u, v, w)  
source, target = map(int, input().split())
result = graph.shortest_distance(source, target)
print(result)