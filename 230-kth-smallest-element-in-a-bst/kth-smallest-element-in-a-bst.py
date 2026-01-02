# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(head,arr):
            if head==None:
                return 
            inorder(head.left,arr)
            arr.append(head.val)
            inorder(head.right,arr)
        
        arr=[]
        inorder(root,arr)
        return arr[k-1]