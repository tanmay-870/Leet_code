class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)

        if arr[0] > arr[1]:
            return 0

        if arr[n-1]>arr[n-2]:
            return n-1

        if n==1:
            return 0

        for i in range (1,n-1):
            if (arr[i]>arr[i+1]) & (arr[i] >arr[i-1]):
                return i
        
    