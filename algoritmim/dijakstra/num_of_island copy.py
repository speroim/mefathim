from typing import List

grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]


def dfs_count_aisled(grid: List[List[str]], row: int, col: int, visited: List[List[bool]])  -> int:
     if row < 0 or col < 0 or row >= len.grid or col >= len.grid[0]:
          