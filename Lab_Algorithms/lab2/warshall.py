# floyd warshall algorith in python

def floyd_warshall(graph):
    # number of vertices in the graph
    V = len(graph)
    
    # initialize closure_graph distance matrix with graph values
    closure_graph = [[float('inf')] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            closure_graph[i][j] = graph[i][j]
    
    # set distance to self as 0
    # for i in range(V):
    #     closure_graph[i][i] = 0
    
    # update distances using Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i == j:
                    closure_graph[i][i] = 0
                else:
                    if closure_graph[i][k] + closure_graph[k][j] < closure_graph[i][j]:
                        closure_graph[i][j] = closure_graph[i][k] + closure_graph[k][j]
    
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
        [0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]
    ]
    
    closure_graph = floyd_warshall(graph)
    print("The shortest distance matrix is:")
    print_graph(closure_graph )
    