class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 'last' pointer track karta hai ki agla non-zero number kis index par aana chahiye
        last = 0
        
        # 'x' pointer poori list ko index 0 se end tak ek-ek karke scan karega
        for x in range(len(nums)):
            # Check karo agar current element non-zero hai
            if nums[x] != 0:
                # Agar non-zero mila, toh use 'last' wale pointer ke element ke sath swap kar do
                # Isse non-zero elements aage aate jayenge aur 0s peeche shift hote jayenge
                nums[last], nums[x] = nums[x], nums[last]
                
                # Ek non-zero number sahi jagah baith gaya, toh agle slot ke liye pointer aage badhao
                last += 1
                
        # Dhyan rahe: Yahan kuch bhi return nahi karna hai kyunki nums in-place update ho raha hai