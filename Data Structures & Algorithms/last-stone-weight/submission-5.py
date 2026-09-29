class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                crash = second - first
                heapq.heappush(stones,-crash) 


        if len(stones) == 0:
            return 0 
        return abs(stones[0])
