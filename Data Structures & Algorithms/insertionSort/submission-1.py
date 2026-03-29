# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs

        result = [pairs.copy()]
        if len(pairs) <= 1:
            return result
        
        i, j = 1, 0
        while i < len(pairs):
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            i += 1
            j = i-1
            result.append(pairs.copy())
        return result
            