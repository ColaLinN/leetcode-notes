from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[j-i for j in range(n)] for i in range(n)]
        print(g)
        def updateG(startIdx, endIdx):
            nonlocal g 
            g[startIdx][endIdx] = 1
            for i in range(startIdx+1):
                for j in range(endIdx, n, 1):
                    g[i][j] = min(g[i][j], g[i][startIdx]+g[endIdx][j])
        res = []
        for q in queries:
            updateG(q[0],q[1])
            res.append(g[0][n-1])
        print(g)
        return res
            