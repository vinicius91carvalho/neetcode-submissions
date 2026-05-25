# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min, max = 1, n
        while min <= max:
            m = min + (max - min) // 2
            res = guess(m)
            if res == 1:
                min = m + 1
            elif res == -1:
                max = m - 1
            else:
                return m
        