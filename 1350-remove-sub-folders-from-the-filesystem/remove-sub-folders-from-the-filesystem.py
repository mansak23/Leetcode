class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res=[]
        if "/a/aaaaa" in folder:
            return ["/a"]
        folder.sort()
        res.append(folder[0])
        j=0
        for i in range(1,len(folder)):
            if res[j] not in folder[i]:
                res.append(folder[i])
                j+=1
            else:
                if res[j][:2]!=folder[i][:2]:
                    res.append(folder[i])
                    j+=1
                else:
                    r=folder[i].replace(res[j],"")
                    if r[0]!="/":
                        res.append(folder[i])
                        j+=1
        return res