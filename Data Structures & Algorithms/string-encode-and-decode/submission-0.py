class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            string_length = []
            while i < len(s) and s[i] != '#':
                string_length.append(s[i])
                i += 1
            string_length = int("".join(string_length))
            # skip #
            i += 1
            string = []
            j = 0
            while i < len(s) and j < string_length:
                string.append(s[i])
                i += 1
                j += 1
            strs.append("".join(string))
        return strs

