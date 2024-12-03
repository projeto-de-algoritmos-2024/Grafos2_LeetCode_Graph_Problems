from collections import defaultdict
import heapq
from typing import List


class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    # montando grafo
    g = defaultdict(dict)
    
    negative_edges = defaultdict(set)
    
    for node, neighbor, value in edges:
      if value == -1:
        negative_edges[node].add(neighbor)
        negative_edges[neighbor].add(node)
        value = 1
        
      g[node][neighbor] = value
      g[neighbor][node] = value
        
    # usando dijkstra para calcular caminho válido.
    heap = [(0, 0, [source])]
    valid_path = None
    path_value = 0
    while heap:
      num_negatives, value, path = heapq.heappop(heap)
      if path[-1] == destination:
        # termine se o valor da soma for o target ou o número de negativos é maior que 0
        if value == target or num_negatives > 0:
          valid_path = path
          path_value = value
        break
      current = path[-1]
      for neighbor in g[current]:
        if neighbor in path:
          continue
        if neighbor in negative_edges[current]:
          new_negatives = num_negatives + 1
        else:
          new_negatives = num_negatives
        if (g[current][neighbor] + value) <= target:
          heapq.heappush(heap, (new_negatives, g[current][neighbor] + value, path + [neighbor]))

    remaining = target - path_value
    
    if not valid_path:
      return []
          
    path_edges = set()
    for i in range(len(valid_path) - 1):
      path_edges.add((valid_path[i], valid_path[i + 1]))
      path_edges.add((valid_path[i + 1], valid_path[i]))
    result_edges = []
    
    for node, neighbor, value in edges:
      if value >= 1:
        result_edges.append([node, neighbor, value])
      elif (node, neighbor) in path_edges:
        result_edges.append([node, neighbor, 1 + remaining])
        remaining = 0
      else:
        result_edges.append([node, neighbor, 2*(10**9)])
    
    return result_edges
          