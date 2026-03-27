class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        res = 0

        for i in range (0, len(nums)-1,2):
            res += nums[i]
        return res    



"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
"""        
