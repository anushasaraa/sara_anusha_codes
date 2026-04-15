class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = _max = _min = nums[0]
        for num in nums[1:]:
            old_max = _max
            _max = max(_min * num, _max * num, num)
            _min = min(_min * num, old_max * num, num)
            ans = max(_max, _min, ans)
        return ans
