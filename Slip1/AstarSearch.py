graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'E': 1},
    'E': {}
}

h = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 1,
    'E': 0
}

start = 'A'
goal = 'E'

open_list = [(h[start], 0, start, [start])]
visited = set()

while open_list:
    f, g, node, path = min(open_list)
    open_list.remove((f, g, node, path))

    if node == goal:
        print("Path:", path)
        print("Cost:", g)
        break

    if node in visited:
        continue

    visited.add(node)

    for n, cost in graph[node].items():
        new_g = g + cost
        new_f = new_g + h[n]
        open_list.append((new_f, new_g, n, path + [n]))