import heapq

goal = "1230"

def h(s):
    return sum(s[i] != goal[i] and s[i] != '0' for i in range(4))

def astar(start):
    pq = [(h(start), start)]
    visited = set()

    while pq:
        f, state = heapq.heappop(pq)

        if state == goal:
            print("Goal Found:", state)
            return

        if state in visited:
            continue
        visited.add(state)

        print(state)

        z = state.index('0')
        r, c = divmod(z, 2)

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 2 and 0 <= nc < 2:
                nz = nr * 2 + nc

                x = list(state)
                x[z], x[nz] = x[nz], x[z]
                new = ''.join(x)

                if new not in visited:
                    heapq.heappush(pq, (h(new), new))

astar("1023")