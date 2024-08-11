from typing import List
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # i, j, k
        # @cache
        def dp(i, j, k):
            if k > len(nums) -1: return 1
            res = 0
            if k == 0:
                for i2 in range(nums[k]+1):
                    # print(i, j, k, i2, nums[k])
                    res += dp(i2, nums[k]-i2, k+1)
            else:
                if i > nums[k]: return 0
                for i2 in range(i, nums[k]+1, 1):
                    # print("second", i, j, k, i2, nums[k])
                    if nums[k] - i2 > j:
                        continue
                    else:
                        res += dp(i2, nums[k]-i2, k+1)
            return res
        return dp(0, 0, 0) % (10 ** 9 + 7)

s = Solution()
# print(s.countOfPairs([2,3,2]))
print(s.countOfPairs([40,40,40,40,41,42,43,44,45,45]))