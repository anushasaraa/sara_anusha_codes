class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        prev = 0
        for i in range(1, 1 << n):
            prev ^= -i&i # Toggle the LSB of i
            ans.append(prev)
        return ans
