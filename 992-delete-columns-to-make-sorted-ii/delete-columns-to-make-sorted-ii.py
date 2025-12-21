class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        sorted_rows = [False] * (rows - 1)
        deletions = 0

        for c in range(cols):
            delete = False

            for r in range(rows - 1):
                if not sorted_rows[r] and strs[r][c] > strs[r + 1][c]:
                    delete = True
                    break

            if delete:
                deletions += 1
                continue

            for r in range(rows - 1):
                if strs[r][c] < strs[r + 1][c]:
                    sorted_rows[r] = True

        return deletions
