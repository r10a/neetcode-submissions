class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        nums.sort()

        def dfs(tracker, curr_sum, start_idx):
            if curr_sum > target:
                return []
            if curr_sum == target:
                self.results.append(tracker.copy())
            if curr_sum < target:
                for idx in range(start_idx, len(nums)):
                    tracker.append(nums[idx])
                    dfs(tracker, curr_sum + nums[idx], idx)
                    tracker.pop()
        
        dfs([], 0, 0)

        return self.results
                        