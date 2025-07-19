class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res:
                res.append(f)
            else:
                prev = res[-1]
                if f.startswith(prev) and len(f) > len(prev) and f[len(prev)] == '/':
                    continue
                else:
                    res.append(f)
        return res
        # res=[]
        # if "/a/aaaaa" in folder:
        #     return ["/a"]
        # folder.sort()
        # res.append(folder[0])
        # j=0
        # for i in range(1,len(folder)):
        #     if res[j] not in folder[i]:
        #         res.append(folder[i])
        #         j+=1
        #     else:
        #         if res[j][:2]!=folder[i][:2]:
        #             res.append(folder[i])
        #             j+=1
        #         else:
        #             r=folder[i].replace(res[j],"")
        #             if r[0]!="/":
        #                 res.append(folder[i])
        #                 j+=1
        # return res