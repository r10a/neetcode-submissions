class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            val = 0
            # print(i, j, text1[i], text2[j])
            if text1[i] == text2[j]:
                val += 1 + dfs(i + 1, j + 1)
            else:
                val += max(dfs(i, j + 1), dfs(i + 1, j))
            
            cache[(i, j)] = val
            return val
        
        return dfs(0, 0)