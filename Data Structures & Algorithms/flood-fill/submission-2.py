class Solution:

    def dfs_matrix(self, image: List[List[int]], rows: int, cols: int, sr: int, sc: int, color: int, origin_color: int) -> List[List[int]]:
        if min(sr, sc) < 0 or sr >= rows or sc >= cols or image[sr][sc] != origin_color:
            return None

        image[sr][sc] = color
        
        self.dfs_matrix(image, rows, cols,  sr + 1, sc, color, origin_color)
        self.dfs_matrix(image, rows, cols, sr - 1, sc, color, origin_color)
        self.dfs_matrix(image, rows, cols, sr, sc + 1, color, origin_color)
        self.dfs_matrix(image, rows, cols, sr, sc - 1, color, origin_color)

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        return self.dfs_matrix(image, ROWS, COLS, sr, sc, color, image[sr][sc])