class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []

        def dfs(tracker, curr_sum, start_idx):
            if curr_sum > target:
                return []
            if curr_sum == target:
                self.results.append(tracker)
            if curr_sum < target:
                for idx in range(start_idx, len(nums)):
                    dfs(tracker + [nums[idx]], curr_sum + nums[idx], idx)
        
        dfs([], 0, 0)

        return self.results
                        