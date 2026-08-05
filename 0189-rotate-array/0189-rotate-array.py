class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # Step 1: Reverse the whole array
        nums.reverse()

        # Step 2: Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse remaining elements
        nums[k:] = reversed(nums[k:])