current = 1
goal = 5

while current != goal:
    print("Current:", current)
    
    if current < goal:
        current = current + 1
        
    else:
        current = current - 1
        
print("Goal Reached:", goal)