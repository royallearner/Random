def floyds(graph):
    for k in range(len(graph)) :
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i==j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

def print_graph(graph):
    V = len(graph)
    for i in range(V):
        for j in range(V):
            if graph[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(graph[i][j], end="\t")
        print()


if __name__ == "__main__":    
    graph = [[999,20,10,999],[999,999,15,999],[999,999,999,40],[999,999,999,999]]
    floyds(graph)
    print_graph(graph)
    
        