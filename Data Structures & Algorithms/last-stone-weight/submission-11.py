class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            stone = abs(stone1) - abs(stone2)
            if stone > 0:
                heapq.heappush(max_heap, -stone)
                heapq.heapify(max_heap)
        if len(max_heap) > 0:
            return abs(max_heap[0])
        return 0