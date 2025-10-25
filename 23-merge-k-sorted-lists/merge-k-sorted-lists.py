# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=None
        ls=[]
        for i in lists:
            while i != None:
                ls.append(i.val)
                i=i.next
        ls.sort(reverse=True)
        print(ls)  
        for i in ls:
            temp=ListNode(i)
            if not res:
                res=temp
            else:
                temp.next=res
                res=temp
        return res