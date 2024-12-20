from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count frequencies
        freq_map = Counter(words)
    
        # Step 2: Use a min-heap
        heap = []
        for word, freq in freq_map.items():
            heapq.heappush(heap, (-freq, word))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])  # Append only the word
            
        return result
       


    