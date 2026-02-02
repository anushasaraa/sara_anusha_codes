def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for a in range(0,len(nums)):
            b=target-nums[a]
            if(b in d):
                return [a,d[b]]
            else:
                d[nums[a]]=a
