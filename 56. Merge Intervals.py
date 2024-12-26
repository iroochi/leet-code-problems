class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        res = []
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        for next in intervals[1:]:
            if curr[1] >= next[0]:
                curr[1] = max(curr[1], next[1])
            else:
                res.append(curr)
                curr = next
        
        res.append(curr)
        return res


            