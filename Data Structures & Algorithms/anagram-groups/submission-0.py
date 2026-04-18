class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for string in strs:
            lookup["".join(sorted(string))].append(string)
        return list(lookup.values())
