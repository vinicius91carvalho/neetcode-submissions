class Solution:

    def dfs_matrix(self, image: List[List[int]], sr: int, sc: int, color: int, origin_color: int, analyzed_vertices: set) -> List[List[int]]:

        ROWS, COLS = len(image), len(image[0])

        if min(sr, sc) < 0 or sr >= ROWS or sc >= COLS or image[sr][sc] != origin_color or (sr, sc) in analyzed_vertices:
            return None

        image[sr][sc] = color
        analyzed_vertices.add((sr, sc))
        
        self.dfs_matrix(image, sr + 1, sc, color, origin_color, analyzed_vertices)
        self.dfs_matrix(image, sr - 1, sc, color, origin_color, analyzed_vertices)
        self.dfs_matrix(image, sr, sc + 1, color, origin_color, analyzed_vertices)
        self.dfs_matrix(image, sr, sc - 1, color, origin_color, analyzed_vertices)

        analyzed_vertices.remove((sr, sc))

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.dfs_matrix(image, sr, sc, color, image[sr][sc], set())