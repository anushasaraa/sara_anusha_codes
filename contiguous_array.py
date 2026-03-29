class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        height = 0  # Our current altitude
        # Store the FIRST time we saw a specific height
        # {altitude: step_index}
        first_time_at = {0: -1} 
        max_dist = 0
        
        for step, val in enumerate(nums):
            if val == 1:
                height += 1  # Climb up
            else:
                height -= 1  # Climb down
            
            if height in first_time_at:
                # If we've been at this altitude before, 
                # calculate the distance from the first time we were here.
                max_dist = max(max_dist, step - first_time_at[height])
            else:
                # Record the first time we reach this new altitude
                # We don't update it if seen again, because we want the longest stretch
                first_time_at[height] = step
                
        return max_dist
