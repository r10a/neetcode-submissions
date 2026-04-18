class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1
            lookup[tuple(key)].append(string)
        return list(lookup.values())
