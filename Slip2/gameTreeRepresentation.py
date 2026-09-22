game = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def display(node, level=0):
    print(" "* level+node)
    
    for child in game[node]:
        display(child, level+1)
        
display('A')