from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        res = []
        for i in range(2, -1, -1):
            x = nums2[0] - nums1[i]
            j = 0
            for n in nums1[i:]:
                # print("test", n, x, nums2[j], j, nums2[j] == n + x)
                if nums2[j] == n + x:
                    j += 1
                if j == len(nums2):
                    # i 越大，nums1[i] 越大，nums2[0] - nums1[i] 越小
                    # 比如有 -2 和 0，我们倾向于返回 -2
                    return x
        return nums2[0] - nums1[0]


s = Solution()
print(s.minimumAddedInteger([4,20,16,12,8], [14,18,10]))
