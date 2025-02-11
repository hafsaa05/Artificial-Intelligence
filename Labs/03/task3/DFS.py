from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_limited_search(self, src, target, depth):
        if src == target:
            return True
        if depth == 0:
            return False
        for neighbor in self.graph[src]:
            if self.depth_limited_search(neighbor, target, depth-1):
                return True
        return False

    def iterative_deepening_search(self, src, target, max_depth):
        for depth in range(max_depth):
            if self.depth_limited_search(src, target, depth):
                return True
        return False

graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

start = 0
end = 6
max_depth = 3
if graph.iterative_deepening_search(start, end, max_depth):
    print(f"Target {end} is reachable from {start} within max depth {max_depth}")
else:
    print(f"Target {end} is NOT reachable from {start} within max depth {max_depth}")
