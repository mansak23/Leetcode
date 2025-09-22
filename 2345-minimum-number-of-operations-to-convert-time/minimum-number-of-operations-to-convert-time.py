class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ct=60*int(current[0:2])+int(current[3:5])
        tt=60*int(correct[0:2])+int(correct[3:5])
        dif=tt-ct
        cnt=0
        for i in [60,15,5,1]:
            cnt+=dif//i
            dif%=i
        return cnt