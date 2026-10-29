class Solution:
    def merge(self, nums1, m, nums2, n):
        # i: nums1 ke aakhiri valid number ka index
        i = m - 1
        
        # j: nums2 ke aakhiri number ka index
        j = n - 1
        
        # k: nums1 ki aakhiri khali jagah (end position)
        k = m + n - 1

        # Jab tak nums2 ke saare numbers place na ho jayein
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1