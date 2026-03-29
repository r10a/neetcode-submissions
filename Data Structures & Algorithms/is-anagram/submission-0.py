class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = defaultdict(int)
        for c in s:
            lookup[c] += 1
        for c in t:
            lookup[c] -= 1
        for key, val in lookup.items():
            if val != 0:
                return False
        return True