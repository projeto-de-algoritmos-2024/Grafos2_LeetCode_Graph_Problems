import collections
import heapq
from typing import List

class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    g = collections.defaultdict(list)

    lines = len(grid)
    colums = len(grid[0])

    walls = [0] * lines * colums
        
    # montando grafo
    for line_num in range(lines):
      for col_num in range(colums):
        # calculando valor do nó baseado nas colunas e linhas
        node_number = col_num + colums * line_num 
        if (col_num + 1) in range(colums):
          # adiciona o vizinho da direita
          neighbor_number = (col_num + 1) + colums * line_num
          g[node_number].append(neighbor_number)
          g[neighbor_number].append(node_number)
        if (line_num + 1) in range(len(grid)):
          # adiciona o vizinho de baixo
          neighbor_number = col_num + colums * (line_num + 1)
          g[node_number].append(neighbor_number)
          g[neighbor_number].append(node_number)
        # adiciona ao vetor que 
        walls[node_number] = grid[line_num][col_num]
    
    # print(g)
    # print(walls)
    
    # dijkstra para encontrar o menor caminho até o último
    path_array = [0] * lines * colums
    last_node = (lines * colums)-1
    heap = [(walls[0], 0, 0)]
    visited = set()
    while (heap):
      # print(heap)
      is_wall, current, prev = heapq.heappop(heap)
      if (current not in visited):
        # print(current, is_wall, prev)
        visited.add(current)
        path_array[current] = is_wall
        if current == last_node: break # para quando chegar no último elemento
        for neighbor in g[current]:
          if neighbor not in visited:
            heapq.heappush(heap, (walls[neighbor] + is_wall, neighbor, current))
    
    # print(path_array)
    return path_array[last_node]
          
print(Solution.minimumObstacles(Solution, [[0,1,1],[1,1,0],[1,1,0]]))
      