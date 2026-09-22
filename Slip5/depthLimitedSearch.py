graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, goal, depth):
    
    if node == goal:
        print("Goal Found:", node)
        return True
    
    if depth == 0:
        return False
    
    for n in graph[node]:
        if dls(n, goal, depth-1):
            return True
    
    return False

dls('A', 'F', 2)