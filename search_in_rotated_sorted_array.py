class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(arr, key, start, end):
            if start > end:
                return -1
            
            mid = start + (end-start)//2
            if arr[mid] == key:
                return mid
            if arr[start] <= arr[mid]:
                if arr[start] <= key and key <= arr[mid]:
                    return helper(arr, key, start, mid-1)
                else:
                    return helper(arr, key, mid+1, end)
            
            if key>=arr[mid] and key<=arr[end]:
                return helper(arr, key, mid+1, end)
            else:
                return helper(arr, key, start, mid-1)
            
                
        return helper(nums, target, 0, len(nums)-1)
