class Solution:
    def numSquares(self, n: int) -> int:
        x = 1
        res = []
        while x*x <= n:
            res.append(x*x)
            x += 1
        
        for i in range(0, len(res)):
            if res[i] == n:
                return 1
        
        for i in range(0, len(res)):
            for j in range(i, len(res)):
                if res[i] + res[j] == n:
                    return 2
        
        for i in range(0, len(res)):
            for j in range(i, len(res)):
                for k in range(j, len(res)):
                    if res[i] + res[j] + res[k] == n:
                        return 3
        return 4

        