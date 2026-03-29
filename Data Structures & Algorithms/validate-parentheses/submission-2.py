class Solution:
    def isValid(self, s: str) -> bool:
        def get_matching_bracket(bracket: str) -> str:
            if bracket == ')':
                return '('
            if bracket == '}':
                return '{'
            if bracket == ']':
                return '['
            raise Error(f'Unknown bracket: {bracket}')
        
        stack = []
        if len(s) <= 1:
            return False
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif stack and stack[-1] == get_matching_bracket(char):
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
                