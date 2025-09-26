class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            ky=''.join(sorted(i))
            res[ky].append(i)
        return list(res.values())