print("Prims Algorithm")
def prims_mst(V, graph):
    visited = [False] * V
    visited[0] = True
    edges = []
    cost = 0

    for _ in range(V - 1):
        min_edge = ( -1, -1, float('inf'))  # u, v, weight
        for u in range(V):
            if visited[u]:
                for v in range(V):
                    if not visited[v] and graph[u][v] != float('inf'):
                        if graph[u][v] < min_edge[2]:
                            min_edge = (graph[u][v], u, v)
        u, v, weight = min_edge
        visited[v] = True
        edges.append((u, v, weight))
        cost += weight
        print(f"{u} -> {v} : {weight}")

    return cost

if __name__ == '__main__':
    V = 5
    graph = [
        [1, float('inf'), 2, 3, 2],
        [1, 6, 3, 2, 4],
        [4, 2, 6, 4, 7,],
        [2, 5, 4, float('inf'), 1],
        [3, 2, 6, 4, 1]
    ]
    total_cost = prims_mst(V, graph)
    print(f"Total cost of MST: {total_cost}")