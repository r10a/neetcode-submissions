class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        def _bin_search(nums, s, e):
            m = s + (e - s) // 2
            
            if nums[m] == target:
                return m

            if (e - s) <= 0:
                return -1
            
            if nums[m] > target:
                return _bin_search(nums, s, m - 1)
            else:
                return _bin_search(nums, m + 1, e)
        
        return _bin_search(nums, 0, len(nums) - 1)
