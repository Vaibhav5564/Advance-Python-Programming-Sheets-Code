graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def valid(node, color):
    for neighbour in graph[node]:
        if result.get(neighbour) == color:
            return False
        return True
    
def solve(node):
    if node == len(graph):
        return True
    
    current = list(graph.keys())[node]
    
    for color in colors:
        if valid(current, color):
            result[current] = color
            
            if solve(node+1):
                return True
            
            del result[current]
            
    return False

solve(0)
print(result)