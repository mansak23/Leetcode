# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        while head != None:
            temp=ListNode(head.val)
            temp.next=res
            res=temp
            head=head.next
        return res