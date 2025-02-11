from collections import defaultdict, deque

# Graph class for IDDFS
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def depth_limited_search(self, src, target, depth):
        if src == target:
            return True
        if depth == 0:
            return False
        for neighbor in self.graph[src]:
            if self.depth_limited_search(neighbor, target, depth - 1):
                return True
        return False

    def iterative_deepening_search(self, src, target, max_depth):
        for depth in range(max_depth):
            if self.depth_limited_search(src, target, depth):
                return True
        return False


# Tree class for IDDFS
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root

    def depth_limited_search(self, node, target, depth):
        if node is None:
            return False
        if node.value == target:
            return True
        if depth == 0:
            return False
        for child in node.children:
            if self.depth_limited_search(child, target, depth - 1):
                return True
        return False

    def iterative_deepening_search(self, target, max_depth):
        for depth in range(max_depth):
            if self.depth_limited_search(self.root, target, depth):
                return True
        return False

graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(7)]
tree = Tree(root)

# Test Iterative Deepening Search for Graph
start = 0
end = 6
max_depth = 3
if graph.iterative_deepening_search(start, end, max_depth):
    print(f"Graph: Target {end} is reachable from {start} within max depth {max_depth}")
else:
    print(f"Graph: Target {end} is NOT reachable from {start} within max depth {max_depth}")

# Test Iterative Deepening Search for Tree
target_value = 6
if tree.iterative_deepening_search(target_value, max_depth):
    print(f"Tree: Target {target_value} is reachable within max depth {max_depth}")
else:
    print(f"Tree: Target {target_value} is NOT reachable within max depth {max_depth}")
