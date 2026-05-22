class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0,0,0]
        for i in range(0, len(nums)):
            counter[nums[i]] += 1

        n = 0
        for i in range(0, len(counter)):
            for j in range(0, counter[i]):
                nums[n] = i
                n += 1
