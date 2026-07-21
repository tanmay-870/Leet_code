class Solution:
    def containsDuplicate(self, nums):
        m = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in m:
                return True
            m[nums[i]] = 1

        return False