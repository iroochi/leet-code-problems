from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_indices = defaultdict(list) 
        for i, char in enumerate(s):
            char_indices[char].append(i)
        count = 0
        for word in words:
            prev = -1
            for char in word:
                indices = char_indices[char]
                idx = bisect.bisect_left(indices, prev + 1) # Find the smallest index greater than prev_index
                if idx == len(indices):
                    break
                prev = indices[idx]
            else:
                count += 1
        return count



