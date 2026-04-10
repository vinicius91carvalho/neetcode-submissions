class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        output = False
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                output = True
                break
        return output
        
