class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        n = len(nums1)
        ans = [0] * n

        order = sorted(range(n), key=lambda i: nums2[i])

        left = 0
        right = n - 1

        for i in reversed(order):
            if nums1[right] > nums2[i]:
                ans[i] = nums1[right]
                right -= 1
            else:
                ans[i] = nums1[left]
                left += 1

        return ans