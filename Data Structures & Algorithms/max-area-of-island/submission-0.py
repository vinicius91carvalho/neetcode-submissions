class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(row, col, counter=1) -> int:
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                dimensions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for d in dimensions:
                    r, c = row + d[0], col + d[1]
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        counter += 1
            
            return counter


        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1 and (x, y) not in visited:
                    size = bfs(x, y)
                    res = max(res, size)
        
        return res