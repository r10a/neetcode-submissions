class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        i = 0
        j = 0
        k = 0
        while i < len(nums):
            curr = nums[i]
            unique.add(curr)
            j = i + 1
            while j < len(nums) and curr == nums[j]:
                j += 1
            if (k + 1) < len(nums) and j < len(nums):
                nums[k + 1] = nums[j]
            k += 1
            i = j
        return len(unique)