class Solution:
    def climbStairs(self, n: int, memoization={}) -> int:
        
        if memoization.get(n):
            return memoization.get(n)
        
        if n == 0:
            return 1
        
        elif n < 0:
            return 0
        
        memoization[n-1] = self.climbStairs(n - 1)
        memoization[n-2] = self.climbStairs(n - 2)
        
        return memoization[n-1] + memoization[n-2]