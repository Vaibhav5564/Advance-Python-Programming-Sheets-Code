from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

queue = deque(['A'])

visited = set()

while queue:
    node = queue.popleft()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for n in graph[node]:
            queue.append(n)
