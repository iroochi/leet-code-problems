from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num, fq in freq.items():
            heapq.heappush(heap, (fq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        
        return [num for fq, num in heap]