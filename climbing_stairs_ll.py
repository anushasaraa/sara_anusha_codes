
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        back1 = back2 = back3 = 0                                   # <-- 1)

        for stepCost in costs:                                      # <-- 2)
            minCost = min(back1 + 1, back2 + 4, back3 + 9)

                                                           
            back1, back2, back3  = stepCost+minCost, back1, back2   # <-- 3)

        return back1                                                # <-- 4)
