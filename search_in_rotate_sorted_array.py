class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return True
            
            # Handle duplicates that obscure the sorted half
            if nums[low] == nums[mid] and nums[high] == nums[mid]:
                low += 1
                high -= 1
                continue
                
            # Check if the left half is the sorted half
            if nums[low] <= nums[mid]:
                # Is the target in this sorted left half?
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Otherwise, the right half must be the sorted half
            else:
                # Is the target in this sorted right half?
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
