class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        res = 0
        while k >= 1:
            res = heapq.heappop(max_heap)
            k -= 1
        return -res
        