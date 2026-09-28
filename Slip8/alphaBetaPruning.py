tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [2, 9]
}

def minimax(node, maximizing):
    if isinstance(node, int):
        return node

    values = [minimax(x, not maximizing) for x in tree[node]]

    if maximizing:
        return max(values)
    else:
        return min(values)

def alphabeta(node, alpha, beta, maximizing):
    if isinstance(node, int):
        return node

    if maximizing:
        value = -999
        for x in tree[node]:
            value = max(value, alphabeta(x, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = 999
        for x in tree[node]:
            value = min(value, alphabeta(x, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value

print("Minimax:", minimax('A', True))
print("Alpha-Beta:", alphabeta('A', -999, 999, True))