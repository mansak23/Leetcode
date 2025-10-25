# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        ls=set()
        while head!=None:
            if head.val not in ls:
                temp=ListNode(head.val)
                ls.add(head.val)
                if res==None:
                    res=temp
                    cur=res
                else:
                    cur.next=temp
                    cur=temp
            head=head.next
        return res