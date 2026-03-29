class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            newRow = [1] * n
            for col in range (n-2, -1, -1):
                newRow[col] = row[col] + newRow[col + 1]
            row = newRow
        return row[0]
