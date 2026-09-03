class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        # Step 1: Find the smallest odd number
        for x in nums1:
            if x % 2 != 0:
                min_odd = min(min_odd, x)

        # If there are no odd numbers, all are even -> True
        if min_odd == float('inf'):
            return True

        # Step 2: Ensure every even number can subtract a smaller odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True