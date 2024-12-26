class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1 / value))
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])  
            visited = set()
        
            while queue:
                node, value = queue.popleft()
                if node == end:
                    return value
                visited.add(node)
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, value * weight))
            
            return -1.0
        
        results = []
        for C, D in queries:
            if C == D and C in graph:
                results.append(1.0)
            else:
                results.append(bfs(C, D))
        
        return results        