class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if len(digits) == 1:
            return list(phone[digits[0]])

        if len(digits) == 2:
            res = []
            for a in phone[digits[0]]:
                for b in phone[digits[1]]:
                    res.append(a + b)
            return res

        if len(digits) == 3:
            res = []
            for a in phone[digits[0]]:
                for b in phone[digits[1]]:
                    for c in phone[digits[2]]:
                        res.append(a + b + c)
            return res

        # len == 4
        res = []
        for a in phone[digits[0]]:
            for b in phone[digits[1]]:
                for c in phone[digits[2]]:
                    for d in phone[digits[3]]:
                        res.append(a + b + c + d)
        return res
