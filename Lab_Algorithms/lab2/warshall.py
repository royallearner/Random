# floyd warshall algorith in python

def floyd_warshall(graph):
    # number of vertices in the graph
    V = len(graph)
    
    # initialize closure_graph distance matrix with graph values
    closure_graph = [[0] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            closure_graph[i][j] = graph[i][j]
    
    # set distance to self as 0
    # for i in range(V):
    #     closure_graph[i][i] = 0
    
    # update distance reachability using Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i == j:
                    closure_graph[i][i] = 0
                else:
                    closure_graph[i][j] = 1 if closure_graph[i][j] or (closure_graph[i][k] and closure_graph[k][j]) else 0
    
    return closure_graph

def print_graph(graph):
    V = len(graph)
    for i in range(V):
        for j in range(V):
            if graph[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(graph[i][j], end="\t")
        print()

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 3, 0, 7],
        [8, 0, 2, 0],
        [5, 0, 0, 1],
        [2, 0, 0, 0]
    ]
    
    closure_graph = floyd_warshall(graph)
    print("\nAdjacency Matrix:")
    print_graph(graph)
    
    print("\nTransitive Closure (Reachability) Matrix:")
    print_graph(closure_graph)
    