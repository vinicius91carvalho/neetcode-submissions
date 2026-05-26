# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculate_balance_and_height(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return (True, 0)

        if not root.left and not root.right:
            return (True, 1)
        
        height_left = self.calculate_balance_and_height(root.left)
        height_right = self.calculate_balance_and_height(root.right)

        height = max(height_left[1], height_right[1])

        balanced = True
        if not height_left[0] or not height_right[0] or abs(height_left[1] - height_right[1]) > 1:
            balanced = False

        return (balanced, height + 1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculate_balance_and_height(root)[0]