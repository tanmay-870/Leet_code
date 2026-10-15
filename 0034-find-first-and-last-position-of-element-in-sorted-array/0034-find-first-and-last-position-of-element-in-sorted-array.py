
class Solution(object):
    def first(self, arr, x):
        n = len(arr)
        low = 0
        high = n-1
        res = -1

        while low <= high:
            mid = (low+high)//2
            if arr[mid] > x:
                high = mid-1
            elif arr[mid] < x:
                low = mid+1
            else:
                res = mid
                high = mid-1

        return res

    def last(self, arr, x):
        n = len(arr)
        low = 0
        high = n-1
        res = -1

        while low <= high:
            mid = (low+high)//2
            if arr[mid] > x:
                high = mid-1
            elif arr[mid] < x:
                low = mid+1
            else:
                res = mid
                low = mid+1

        return res

    def searchRange(self, nums, target):
        arr = nums
        x = target
        f1 = self.first(arr, x)
        l1 = self.last(arr, x)
        return [f1, l1]
