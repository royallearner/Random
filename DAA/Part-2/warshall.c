// floyd warshall algorithm in c to find closure of a graph.
// The graph is represented as an adjacency matrix.
// If there is an edge from i to j, then graph[i][j] is 1, else 0.
// The closure of the graph is represented as a matrix reach[][] such that
// reach[i][j] is 1 if there is a path from i to j, else 0.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int max(a,b){
    if(a>b)
    return a;
    else
    return b;
}

void warshall(int graph[][10], int n, int reach[][10]) {
    int i, j, k;
    // Initialize the reachability matrix with the given graph
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            reach[i][j] = graph[i][j];

    // Update the reachability matrix
    for (j = 0; j < n; j++) {
        for (k = 0; k < n; k++) {
            for (i = 0; i < n; i++) {
                reach[i][j] = max(reach[i][j], (reach[i][k] && reach[k][j]));
            }
        }
    }
}

void main(){
    int graph[10][10], reach[10][10];
    int n, i, j;

    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix of the graph (0 or 1):\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);

    warshall(graph, n, reach);

    printf("The transitive closure of the graph is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {  
            printf("%d ", reach[i][j]);
        }
        printf("\n");
    }
}