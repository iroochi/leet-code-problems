from collections import Counter # counts the occurrences of elements in an iterable
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        # example: nums = [1, 1, 1, 2, 2, 3] ; output: Counter({1: 3, 2: 2, 3: 1})

        heap = []
        for num, fq in freq.items():
            heapq.heappush(heap, (fq, num)) # [(1, 3), (3, 1), (2, 2)]
            if len(heap) > k:
                heapq.heappop(heap)

        
        return [num for fq, num in heap]