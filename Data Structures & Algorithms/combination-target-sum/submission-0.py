class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Base cases
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # Include nums[i] again (stay at i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            
            # Skip nums[i], move to next (go to i+1)
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res