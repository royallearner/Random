import math

# A large value to represent "no edge" or infinity
INF = float('inf')

def prims_mst(V, graph):
    """
    Finds the Minimum Spanning Tree (MST) cost using Prim's algorithm.
    V: Number of vertices.
    graph: V x V adjacency matrix where graph[u][v] is the weight of the edge (u, v).
    """
    
    # 1. Initialization
    # key[i]: The weight of the cheapest edge connecting vertex i to the MST
    key = [INF] * V 
    
    # parent[i]: Stores the parent of vertex i in the MST
    parent = [None] * V 
    
    # mst_set[i]: True if vertex i is included in MST
    mst_set = [False] * V
    
    # Start with the first vertex (index 0)
    key[0] = 0
    parent[0] = -1 # Root of the MST
    
    edges = []
    total_cost = 0

    # 2. Iterate to build the MST (V-1 edges)
    for _ in range(V):
        
        # 2a. Find the minimum key value vertex not yet included in MST
        min_key = INF
        u = -1 # Index of the vertex with the minimum key
        
        for v in range(V):
            if key[v] < min_key and not mst_set[v]:
                min_key = key[v]
                u = v
        
        # If u is still -1, the graph is disconnected
        if u == -1 and _ < V:
            print("Graph is disconnected. MST cannot span all vertices.")
            return total_cost # Return cost up to this point
        
        # Add the selected vertex 'u' to the MST
        mst_set[u] = True
        total_cost += key[u]
        
        # Record the edge added, unless it's the starting node (u=0, parent[u]=-1)
        if parent[u] != -1:
            edge_weight = graph[parent[u]][u]
            edges.append((parent[u], u, edge_weight))
            print(f"Edge added: {parent[u]} -> {u} (Weight: {edge_weight})")

        # 2b. Update key values of adjacent vertices
        # Only consider vertices 'v' that are not yet in the MST
        for v in range(V):
            # Check if there is an edge (u, v) AND v is not in the MST AND the edge weight 
            # is less than the current key[v]
            edge_weight = graph[u][v]
            if not mst_set[v] and edge_weight < key[v]:
                key[v] = edge_weight
                parent[v] = u
                
    print("\nMST Edges (u -> v : weight):")
    for u, v, weight in edges:
        print(f"{u} -> {v} : {weight}")
        
    return total_cost

# Example usage with a valid V x V Adjacency Matrix
if __name__ == '__main__':
    V = 5
    # The adjacency matrix for an undirected graph must be symmetric.
    # INF represents no direct edge.
    graph = [
        # 0     1     2     3     4
        [ 0,    2,   INF,  6,   INF ], # 0
        [ 2,    0,    3,   8,    5  ], # 1
        [ INF,  3,    0,  INF,   7  ], # 2
        [ 6,    8,   INF,  0,    9  ], # 3
        [ INF,  5,    7,   9,    0  ]  # 4
    ]
    
    print("Prims Algorithm")
    total_cost = prims_mst(V, graph)
    print(f"\nTotal cost of MST: {total_cost}")