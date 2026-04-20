class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        result = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            curr_seq = 1
            curr_num = num
            seen.add(curr_num)
            while (curr_num + 1 in lookup):
                curr_seq += 1
                curr_num += 1
                seen.add(curr_num)
            result = max(result, curr_seq)
        
        return result