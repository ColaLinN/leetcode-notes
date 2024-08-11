from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                return dp(i+1, j+1) +1
            return max(dp(i+1, j), dp(i, j+1))
            # for i2 in range(i, len(nums1), 1):
            #     for j2 in range(j, len(nums2), 1):
            #         if 
        return dp(0, 0)
        # s, t = nums1, nums2
        # n, m = len(s), len(t)
        # @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if s[i] == t[j]:
        #         return dfs(i - 1, j - 1) + 1
        #     return max(dfs(i - 1, j), dfs(i, j - 1))
        # return dfs(n - 1, m - 1)