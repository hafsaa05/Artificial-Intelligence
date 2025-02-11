from collections import deque

# Graph class for Bidirectional Search
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start, target, visited, parent):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        return False

    def bidirectional_search(self, start, target):
        if start == target:
            return True

        visited_from_start = [False] * self.num_vertices
        visited_from_target = [False] * self.num_vertices
        parent_from_start = [-1] * self.num_vertices
        parent_from_target = [-1] * self.num_vertices

        visited_from_start[start] = True
        visited_from_target[target] = True

        queue_from_start = deque([start])
        queue_from_target = deque([target])

        while queue_from_start and queue_from_target:
            if self.bfs(start, target, visited_from_start, parent_from_start):
                return True
            if self.bfs(target, start, visited_from_target, parent_from_target):
                return True
        return False


# Tree class for Bidirectional Search
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root

    def bfs(self, node, target, visited, parent):
        if node is None:
            return False
        queue = deque([node])
        visited[node.value] = True
        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return True
            for child in current_node.children:
                if not visited[child.value]:
                    visited[child.value] = True
                    parent[child.value] = current_node.value
                    queue.append(child)
        return False

    def bidirectional_search(self, start, target):
        if start == target:
            return True

        visited_from_start = [False] * 100  
        visited_from_target = [False] * 100
        parent_from_start = [-1] * 100
        parent_from_target = [-1] * 100

        visited_from_start[start] = True
        visited_from_target[target] = True

        queue_from_start = deque([self.root])
        queue_from_target = deque([target])

        while queue_from_start and queue_from_target:
            if self.bfs(self.root, target, visited_from_start, parent_from_start):
                return True
            if self.bfs(target, start, visited_from_target, parent_from_target):
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

# Test Bidirectional Search for Graph
start = 0
end = 6
if graph.bidirectional_search(start, end):
    print(f"Graph: Target {end} is reachable from {start} using bidirectional search")
else:
    print(f"Graph: Target {end} is NOT reachable from {start} using bidirectional search")

# Test Bidirectional Search for Tree
start_value = 1
target_value = 6
if tree.bidirectional_search(start_value, target_value):
    print(f"Tree: Target {target_value} is reachable from {start_value} using bidirectional search")
else:
    print(f"Tree: Target {target_value} is NOT reachable from {start_value} using bidirectional search")
