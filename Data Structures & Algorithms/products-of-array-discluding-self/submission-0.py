class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for idxo, n in enumerate(nums):
            for idxi in range(len(result)):
                if idxi != idxo:
                    result[idxi] *= n
        return result