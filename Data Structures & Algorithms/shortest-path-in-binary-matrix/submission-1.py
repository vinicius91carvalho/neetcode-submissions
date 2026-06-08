class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque()

        if grid[0][0] == 1:
            return -1
        
        visited.add((0, 0))
        queue.append((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

                for dr, dc in directions:
                    rdr, rdc = r + dr, c + dc
                    if min(rdr, rdc) < 0 or rdr == ROWS or rdc == COLS or (rdr, rdc) in visited or grid[rdr][rdc] == 1:
                        continue
                    visited.add((rdr, rdc))
                    queue.append((rdr, rdc))
            length += 1

        return -1