# LeetCode 26: Remove Duplicates from Sorted Array
# Approach: Two Pointers (Slow & Fast Pointer)
# Time Complexity: O(n) | Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        # Base Case: Agar array empty hai toh unique elements 0 honge
        if not nums:
            return 0
        
        # 'k' hamara SLOW POINTER hai:
        # 1. Yeh batata hai ki agla unique number kis index par place karna hai.
        # 2. Pehla element (index 0) hamesha unique hota hai, isliye hum index 1 se bharna shuru karte hain (k = 1).
        k = 1
        
        # 'i' hamara FAST POINTER hai:
        # Yeh index 1 se lekar end tak har element ko explore karta hai.
        for i in range(1, len(nums)):
            
            # Sorted array ka rule:
            # Agar current element 'nums[i]' aakhiri save kiye gaye unique element 'nums[k-1]' se alag hai,
            # iska matlab hume ek NAYA unique number mil gaya hai.
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Us naye number ko valid unique position (k) par copy karo
                k += 1             # Unique elements ka count aur write-index ek aage badhao
        
        # DHYAN RAHE: 'return k' loop ke BAHAR hona chahiye,
        # taaki poora array check hone ke baad total unique elements ka count return ho.
        return k