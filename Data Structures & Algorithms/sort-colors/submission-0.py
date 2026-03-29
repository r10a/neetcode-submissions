class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for n in nums:
            counter[n] += 1
        
        it = 0
        for key, freq in enumerate(counter):
            for i in range(freq):
                nums[it] = key
                it += 1
        