class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left < len(numbers):
            right = left + 1
            while right < len(numbers) and (numbers[left] + numbers[right]) < target:
                right += 1
            if right >= len(numbers):
                left += 1
                continue
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            left += 1