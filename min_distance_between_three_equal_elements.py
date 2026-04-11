class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        leng = len(nums)
        first = [-1] * (leng + 1)
        second = [-1] * (leng + 1)
        high = leng * 2
        res = high

        for idx in range(leng):
            val = nums[idx]
            pos = idx
            fir = first[val]
            sec = second[val]
            first[val], second[val] = sec, pos

            if fir>-1:
                res = min(res, 2 * (pos - fir))

        return  -1 if res == high else res
