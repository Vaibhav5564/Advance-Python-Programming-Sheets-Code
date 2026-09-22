graph = {
    'v1': [('v2', 2), ('v3', 4)],
    'v2': [('v4', 3)],
    'v3': [('v4', 1)],
    'v4': [('v5', 2)],
    'v5': []
}

h = {
    'v1': 6, 
    'v2': 4, 
    'v3': 3,
    'v4': 2,
    'v5': 0
}

open_list = [(h['v1'], 0, 'v1', ['v1'])]

while open_list:
    f, g, node, path = min(open_list)
    open_list.remove((f, g, node, path))
    
    if node == 'v5':
        print("Shortest Path:", path)
        print("Cost:", g)
        break
    
    for next_node, cost in graph[node]:
        new_g = g + cost
        new_f = new_g + h[next_node]
        
        open_list.append(
            (new_f, new_g, next_node, path + [next_node])
        )