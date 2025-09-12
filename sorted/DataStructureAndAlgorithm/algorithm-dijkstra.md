# Dijkstra's Algorithm

Starting position

 `visit[]`: visited nodes, 
 
- 1 for visited, 0 for unvisited
 
`dist[]`: current shortest distance from the starting node to other nodes

`middle`: intermediate node

`path[]`:

1. Initialize `dist[]`
2. Select `middle`, satisfying `visit[middle] == 0` and `dist[middle]` is the minimum
3. Mark `visit[middle] = 1;` 
4. Update `dist[]`