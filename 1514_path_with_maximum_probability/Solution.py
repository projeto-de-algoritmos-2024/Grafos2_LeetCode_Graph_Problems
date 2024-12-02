import collections
import heapq
from typing import List

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    # construindo o grafo
    g = collections.defaultdict(list)

    for i in range(len(edges)):
      a, b = edges[i]
      g[a].append((succProb[i], b))
      g[b].append((succProb[i], a))
    
    # algoritmo de dijkstra para encontrar o melhor caminho
    heap = [(-1, start_node)] # usar probabilidade negativa por conta da heap de mínimo
    visited = set()
    max_prob_path = [0] * n # guardar as probabilidades
    while heap:
      prob, current = heapq.heappop(heap)
      if current not in visited:
        visited.add(current)
        max_prob_path[current] = -prob
        if (current == end_node): break # parar quando chegar no destino
        for neighbour_prob, neighbour in g[current]:
          if neighbour not in visited:
            heapq.heappush(heap, (neighbour_prob * prob, neighbour))
    
    # retornar caminho de maior probabilidade para o destino
    return max_prob_path[end_node] 

print(Solution.maxProbability(Solution, 5, [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]], [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77], 0, 3))