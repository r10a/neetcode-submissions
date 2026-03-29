class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        
        def _search(nums, l, r):
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if l == r:
                return -1
            
            search_left = _search(nums, l, m)
            search_right = _search(nums, m + 1, r)

            return max(search_left, search_right)
        
        return _search(nums, 0, len(nums)-1)