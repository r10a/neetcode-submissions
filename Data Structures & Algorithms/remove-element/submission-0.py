class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def delete(nums, i):
            for i in range(i + 1, len(nums)):
                nums[i-1] = nums[i]
        
        k = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                delete(nums, i)
                k -= 1
        return k