def tsp(cost, visited, curr, count, n, cost_so_far, start, best):
    if count == n and cost[curr][start] != float('inf'):
        return min(best, cost_so_far + cost[curr][start])

    for city in range(n):
        if not visited[city] and cost[curr][city] != float('inf'):
            visited[city] = True
            best = tsp(cost, visited, city, count + 1, n,
                       cost_so_far + cost[curr][city], start, best)
            visited[city] = False
    return best

if __name__ == "__main__":
    cost = [
        [float('inf'), 10, 15, 20],
        [10, float('inf'), 35, 25],
        [15, 35, float('inf'), 30],
        [20, 25, 30, float('inf')]
    ]

    n = len(cost)
    visited = [False] * n
    start = 0
    visited[start] = True
    answer = tsp(cost, visited, start, 1, n, 0, start, float('inf'))
    print("Minimum TSP tour cost:", answer)
