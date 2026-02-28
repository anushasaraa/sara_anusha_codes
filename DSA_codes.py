import heapq
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w=1):
        self.graph[u].append((v, w))

    # ---------------- BFS ----------------
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

    # ---------------- DFS ----------------
    def dfs_util(self, node, visited, result):
        visited[node] = True
        result.append(node)
        
        for neighbor, _ in self.graph[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, result)

    def dfs(self, start):
        visited = [False] * self.V
        result = []
        self.dfs_util(start, visited, result)
        return result

    # ---------------- Dijkstra ----------------
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            current_dist, node = heapq.heappop(pq)
            
            for neighbor, weight in self.graph[node]:
                if dist[neighbor] > current_dist + weight:
                    dist[neighbor] = current_dist + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return dist

    # ---------------- Topological Sort ----------------
    def topo_sort_util(self, node, visited, stack):
        visited[node] = True
        
        for neighbor, _ in self.graph[node]:
            if not visited[neighbor]:
                self.topo_sort_util(neighbor, visited, stack)
        
        stack.append(node)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if not visited[i]:
                self.topo_sort_util(i, visited, stack)
        
        return stack[::-1]


# ---------------- Disjoint Set ----------------
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# ---------------- Main ----------------
if __name__ == "__main__":
    g = Graph(6)
    
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 5, 2)

    print("BFS:", g.bfs(0))
    print("DFS:", g.dfs(0))
    print("Dijkstra:", g.dijkstra(0))
    print("Topological Sort:", g.topological_sort())

    ds = DisjointSet(6)
    ds.union(0, 1)
    ds.union(2, 3)
    print("Find(1):", ds.find(1))
