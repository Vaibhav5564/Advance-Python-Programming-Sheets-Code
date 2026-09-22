from collections import deque

A, B = 4, 3
goal = 2

queue = deque([(0, 0)])

visited = set()

while queue:
    a, b = queue.popleft()
    
    if(a, b) in visited:
        continue
    
    visited.add((a, b))
    print((a, b))
    
    if a == goal or b == goal:
        print("Goal Reached")
        break
    
    states = [
        (A, b),
        (a, B),
        (0, b),
        (a, 0),
        (a - min(a, B-b), b + min(a, B-b)),
        (a + min(b, A-a), b - min(b, A-a))
    ]
    
    for state in states:
        if state not in visited:
            queue.append(state)