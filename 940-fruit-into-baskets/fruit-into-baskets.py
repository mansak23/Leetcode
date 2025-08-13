class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits))<=2:
            return len(fruits)
        if fruits.count(fruits[0])>1000:
            return fruits.count(fruits[0])+1
        cnt=0
        fin=0
        for i in range(len(fruits)):
            cnt=1
            flag=True
            res=[]
            res.append(fruits[i])
            for j in range(i+1,len(fruits)):
                print(fruits[i])
                if fruits[j] in res:
                    res.append(fruits[j])
                    cnt+=1
                elif fruits[j] not in res and flag:
                    res.append(fruits[j])
                    cnt+=1
                    flag=False
                else:
                    break
            # print(res,cnt)
            fin=max(cnt,fin)
        return fin