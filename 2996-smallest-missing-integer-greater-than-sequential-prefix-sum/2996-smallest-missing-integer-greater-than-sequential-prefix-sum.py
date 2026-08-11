class Solution:

    def missingInteger(self, nums: list[int]) -> int:
        #long wale ka sum pta krenge 
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        # yha pr store kr lenge
        num_set = set(nums)

       # konsa reh gya find krenge idr
        while prefix_sum in num_set:
            prefix_sum += 1

        return prefix_sum