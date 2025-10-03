# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val=[]
        def post(temp):
            if not temp:
                return
            post(temp.left)
            post(temp.right)
            val.append(temp.val)
        post(root)
        return val