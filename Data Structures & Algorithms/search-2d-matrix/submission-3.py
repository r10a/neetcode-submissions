class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 and n == 1:
            return matrix[0][0] == target

        def _get(idx):
            i,j = idx // n, idx % n
            return matrix[i][j]

        def _bin_search(arr, s, e):
            m = s + (e - s) // 2
            curr = _get(m)

            if curr == target:
                return True
            
            if e <= s:
                return False
            
            if curr > target:
                return _bin_search(arr, s, m - 1)
            else:
                return _bin_search(arr, m + 1, e)
        
        return _bin_search(matrix, 0, (m*n) - 1)
