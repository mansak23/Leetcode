class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e=sorted(e,key=lambda x:(x[0],-x[1]))
        res=[]
        for _,h in e:
            l,r=0,len(res)-1
            while l<=r:
                mid=(l+r)>>1
                if res[mid]>=h:
                    r=mid-1
                else:
                    l=mid+1
            ind=l
            if ind==len(res):
                res.append(h)
            else:
                res[ind]=h
        return len(res)