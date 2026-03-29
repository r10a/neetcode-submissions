# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        s, e = 0, n
        curr_guess = -1
        while curr_guess != 0:
            m = s + (e - s) // 2

            curr_guess = guess(m)

            if curr_guess == 0:
                return m
            elif curr_guess == -1:
                e = m - 1
            else:
                s = m + 1