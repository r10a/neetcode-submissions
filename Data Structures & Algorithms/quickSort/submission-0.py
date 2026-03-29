# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# 4 8 2 6 7
# 4 8 2 6 7
# 4 2 8 6 7
# 4 2 6 8 7
# 4 2 6 7 8

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def _quick_sort(arr, s, e):
            if e - s <= 0:
                return
            
            pivot = e
            left = s

            for i in range(s, e):
                if arr[i].key < arr[pivot].key:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1
            
            arr[left], arr[pivot] = arr[pivot], arr[left]

            _quick_sort(arr, s, left - 1)
            _quick_sort(arr, left + 1, e)
        
        _quick_sort(pairs, 0, len(pairs) - 1)

        return pairs