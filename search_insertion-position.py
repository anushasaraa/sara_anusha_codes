class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if(target>nums[i]):
                if(target==nums[i]):
                    return i
                elif(i==len(nums)-1):
                    return i+1
            else:
                return i
        

        
