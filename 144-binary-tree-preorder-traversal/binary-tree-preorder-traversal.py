# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val=[]
        def pre(temp):
            if not temp:
                return
            val.append(temp.val)
            pre(temp.left)
            pre(temp.right)
        pre(root)
        return val