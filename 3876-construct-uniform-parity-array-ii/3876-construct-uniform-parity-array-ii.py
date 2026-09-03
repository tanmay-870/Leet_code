class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Minimum element find karo
        min_val = min(nums1)

        # Agar sabse chhota element odd hai, toh humesha sabko odd banaya ja sakta hai
        if min_val % 2 != 0:
            return True

        # Agar sabse chhota even hai, toh check karo kya poori array hi even hai
        for x in nums1:
            if x % 2 != 0:
                # Even min hone ke bawajood odd present hai -> impossible
                return False

        return True