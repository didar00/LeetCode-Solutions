# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_ = 0
        
        def zigzag(node, is_left, count):
            
            if not node:
                return
            
            self.max_ = max(self.max_, count)
            
            if is_left:
                zigzag(node.right, False, count+1)
                zigzag(node.left, True, 1)
            else:
                zigzag(node.left, True, count+1)
                zigzag(node.right, False, 1)

            
        zigzag(root.left, True, 1)
        zigzag(root.right, False, 1)

        return self.max_ 