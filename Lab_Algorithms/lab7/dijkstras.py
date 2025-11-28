print("Dijkstras alggortithm")
import heapq

def dijkstras(graph, start):
    V = len(graph)
    distances = [float('inf')] * V
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # if current_distance > distances[current_vertex]:
        #     continue

        for neighbor in range(V):
            weight = graph[current_vertex][neighbor]
            if weight != float('inf'):
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


graph = [[4, 3, 6],
         [5, 3, 4],
         [8, 6, 4]]

print(dijkstras(graph, 0))


#############

# Dijkstra's Algorithm implementation without using the heapq (priority queue) module.
# This implementation has a time complexity of O(V^2), where V is the number of vertices.

# def dijkstras_no_heapq(graph, start):    
#     V = len(graph)
#     visited = [False] * V
#     distances = [float('inf')] * V

#     distances[start] = 0
    
#     for _ in range(V):
#         min_distance = float('inf')
#         u = -1  # u will store the index of the next closest unvisited node

#         for i in range(V):
#             if not visited[i] and distances[i] < min_distance:
#                 min_distance = distances[i]
#                 u = i
        
#         if u == -1:
#             break
            
#         visited[u] = True
        
#         for v in range(V):
#             weight = graph[u][v]

#             if not visited[v] and weight > 0:
#                 if distances[u] + weight < distances[v]:
#                     distances[v] = distances[u] + weight
    
#     return distances

# graph = [[4, 3, 6],
#          [5, 3, 4],
#          [8, 6, 4]]

# result_distances = dijkstras_no_heapq(graph, 0)
# print(f"Shortest distances from Node 0: {result_distances}")

# Expected output based on previous manual calculation: [0, 3, 6]
