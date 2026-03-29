class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for n in nums:
            for r in range(len(result)):
                result.append(result[r] + [n])

        return result

