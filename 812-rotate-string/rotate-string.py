class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            sub=goal[i+1:]+goal[:i+1]
            if sub == s:
                return True
        return False