def f(x):
    return -x*x+4*x

x=0

while True:
    current = f(x)
    left = f(x-1)
    right = f(x+1)
    
    if right > current:
        x = x+1
    
    elif left > current:
        x = x-1
    
    else:
        break
    
print("x =", x)
print("Maximum ", f(x))