class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        # Pehle array ke elements ka set bana liya fast lookup ke liye O(1)
        st = set(nums)
        
        mn = min(nums)
        mx = max(nums)
        
        ans = []
        
        # Range mn se mx tak check kar rahe hain
        for x in range(mn, mx + 1):
            if x not in st:
                ans.append(x)
                
        return ans