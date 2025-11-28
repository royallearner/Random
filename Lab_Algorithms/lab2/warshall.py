# floyd warshall algorith in python

def floyd_warshall(graph):
    # number of vertices in the graph
    V = len(graph)
    
    # initialize distance matrix with graph values
    dist = [[float('inf')] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # set distance to self as 0
    # for i in range(V):
    #     dist[i][i] = 0
    
    # update distances using Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i == j:
                    dist[i][i] = 0
                else:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_solution(dist):
    V = len(dist)
    for i in range(V):
        for j in range(V):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]
    ]
    
    dist = floyd_warshall(graph)
    print("The shortest distance matrix is:")
    print_solution(dist)
    