from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

start = 'A'
goal = 'E'

queue = deque([[start]])
visited = set()

while(queue):
    path = queue.popleft()
    node = path[-1]
    
    if node == goal:
        print("Goal Reached")
        print("Path", path)
        break
    
    if node not in visited:
        visited.add(node)
        
        for n in graph[node]:
            queue.append(path+[n])