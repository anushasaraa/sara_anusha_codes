class Solution:
    def countSubarraysLengthThreeOrMore(self, n: int) -> int:
        # A subarray needs at least 3 elements. 
        # If the array is shorter than 3, no such subarray exists.
        if n < 3:
            return 0
    
        # Mathematical Formula:
        # Total subarrays: n*(n+1) // 2
        # Subarrays of length 1: n
        # Subarrays of length 2: n - 1
        # Result = Total - (Len 1) - (Len 2)
    
        total = (n * (n + 1)) // 2
        result = total - n - (n - 1)
        #print(f"total amount of subarrays larger than 3 for {n} is {result}")
        return result

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        if nums[-2] != nums[-1]:
            nums.append(nums[-2])
        else:
            nums.append(nums[-1]-nums[-2]-1)
        l = len(nums)

        result = 0
        
        current_diff = nums[1] - nums[0]
        current_length = 2
        current_pos = 2

        while current_pos < l:
            new_diff = nums[current_pos] - nums[current_pos - 1]
            if new_diff == current_diff:
                current_length += 1
            else:

                result += self.countSubarraysLengthThreeOrMore(current_length)
                current_length = 2
                current_diff = new_diff
            current_pos += 1 

        return result
