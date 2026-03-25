class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False  
        first_count = Counter(s)
        sec_count = sum(1 for count in first_count.values() if count % 2 != 0)
        return sec_count <= k



        
        
