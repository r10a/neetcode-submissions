class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)

        def twoSum(left_bound, right_bound, target):
            results = []
            if left_bound < 0 or right_bound >= len(nums):
                return []
            left, right = left_bound, right_bound
            while left < right and left >= left_bound and right <= right_bound:
                curr_sum = nums[left] + nums[right]
                # print(left, right, nums[left], nums[right], curr_sum, target)
                if curr_sum > target:
                    right -= 1
                if curr_sum < target:
                    left += 1
                if curr_sum == target:
                    results.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
            return results

        results = []
        for idx, n in enumerate(nums[:-2]):
            if idx > 0 and n == nums[idx-1]:
                continue
            curr_results = twoSum(idx+1, len(nums) - 1, -n)            
            if curr_results:
                for result in curr_results:
                    results.append([n, result[0], result[1]])

        return results
                