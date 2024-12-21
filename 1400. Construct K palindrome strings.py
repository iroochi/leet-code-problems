from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        freq = Counter(s)
        odd_count = sum(count % 2 != 0 for count in freq.values())
                
        return odd_count <= k