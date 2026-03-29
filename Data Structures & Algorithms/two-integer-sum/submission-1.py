class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(list)
        for idx, num in enumerate(nums):
            lookup[num].append(idx)
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in lookup:
                for pair_idx in lookup[pair]:
                    if pair_idx != idx:
                        return [idx, pair_idx]
            