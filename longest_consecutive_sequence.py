class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0 or n == 1:
            return n

        remove_dup = set(nums)
        max_sub = 1

        for curr_ele in remove_dup:
            # only start if curr_ele is the start of sequence
            if curr_ele - 1 not in remove_dup:
                next_ele = curr_ele + 1
                curr_sub = 1

                while next_ele in remove_dup:
                    curr_sub += 1
                    next_ele += 1

                max_sub = max(max_sub, curr_sub)

        return max_sub
