"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        queue = collections.deque()
        queue.append(node)
        clones_map = {}

        if not node:
            return None
        
        def reuse_or_create(node: Optional['Node']):
            if node.val in clones_map:
                return clones_map[node.val]
            clones_map[node.val] = Node(node.val, [])
            return clones_map[node.val]

        root = None
        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            clone = reuse_or_create(node)

            if not root:
                root = clone

            if node.neighbors:
                for neighbor in node.neighbors:
                    clone_neighbor = reuse_or_create(neighbor)
                    clone.neighbors.append(clone_neighbor)
                    queue.append(neighbor)
            
            visited.add(node)
        
        return root