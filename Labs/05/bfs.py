tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'file'],
    'D': [],
    'E': ['H', 'I']
}

def BFS(tree, start, goal):
    visited = set()  
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nNode found!")
            return  

        for child in tree.get(node, []):  # Use .get() to avoid KeyError
            if child not in visited:
                visited.add(child)
                queue.append(child)

    print("\nNode not found!") 

start = 'A'
goal = "file"

print("BFS Algorithm:\n")  
BFS(tree, start, goal)
