graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ["Red", "Green", "Blue"]
result = {}

def valid(node, color):
    for n in graph[node]:
        if(result.get(n) == color):
            return False
        return True
    
def solve(nodes):
    if not nodes:
        return True
    
    node = nodes[0]
    
    for color in colors:
        if valid(node, color):
            result[node] = color
            
            if solve(node[1:]):
                return True
            
            del result[node]
            
    return False

solve(list(graph.keys()))

print(result)