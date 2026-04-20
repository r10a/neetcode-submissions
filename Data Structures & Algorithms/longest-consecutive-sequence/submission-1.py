class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        result = 0
        for num in nums:
            curr_seq = 1
            curr_num = num
            while (curr_num + 1 in lookup):
                curr_seq += 1
                curr_num += 1
            result = max(result, curr_seq)
        
        return result