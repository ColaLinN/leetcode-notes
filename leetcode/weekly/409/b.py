from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # O(n^3)
        # g = [[j-i for j in range(n)] for i in range(n)]
        # res = []
        # for q in queries:
        #     startIdx, endIdx = q[0], q[1]
        #     g[startIdx][endIdx] = 1
        #     for i in range(startIdx+1):
        #         for j in range(endIdx, n, 1):
        #             g[i][j] = min(g[i][j], g[i][startIdx]+g[endIdx][j]+1)
        #     res.append(g[0][n-1])
        # return res

        # O(n^2)
        def backtrace(i):
            nonlocal d
            if i == n-1: return 0
            l = n-i-1
            for j in range(i, n, 1):
                if j in d:
                    for k in d[j]:
                        l = min(l, backtrace(k)+1+j-i)
            return l
        d = dict()
        res = []
        cq = []
        for q in queries:
            if q[0] in d:
                d[q[0]].append(q[1])
            else:
                d[q[0]] = [q[1]]
            # cq.append(q)
            # cq.sort(key = lambda q:q[0])
            res.append(backtrace(0))
        return res

# For the above code, the following is the output when executed:
s = Solution()
print(s.shortestDistanceAfterQueries(16, [[1,9],[5,14],[10,13],[3,15]]
))
            