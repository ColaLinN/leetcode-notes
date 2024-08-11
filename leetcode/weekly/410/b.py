class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # i, j, k
        # lessI = 0
        # mx = max(nums)
        # if nums[0] != mx:
        irMx = nums[-1]
        jlMx = nums[0]
        mxIs = []
        cMx = 0
        for j in range(len(nums)-1, -1, -1):
            mxIs.append(max(cMx, nums[j]))
        mxIs = mxIs[::-1]
        # print(mxIs)
        @cache
        def dp(i, j, k):
            if k > len(nums) - 1:
                return 1
            res = 0
            if i > nums[k]:
                return 0
            for i2 in range(i, nums[k] - j +1, 1):
                if nums[k] - i2 > j:
                    continue
                elif i2 > mxIs[k]:
                    break
                elif k < len(nums) - 1 and nums[k + 1] < i2:
                    continue
                elif irMx < i:
                    # print("skip")
                    break
                elif k == len(nums) -1:
                    res += 1
                else:
                    res += dp(i2, nums[k] - i2, k + 1)
            return res
        res = 0
        for i2 in range(min(nums[0] + 1, irMx+1)):
            # print(i2, irMx)
            if i2 > mxIs[0]:
                break
            else:
                res += dp(i2, nums[0] - i2, 1)
        return res % (10**9 + 7)