'''
algo:
    - count letters in a dict
    - go through the count:
        - take (val//2)*2 and add it to ans
    - if extra char availble, add 1

Time: O(N)
Space: O(52)
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        longest_pal_len = 0
        for val in count.values():
            longest_pal_len += (val//2) * 2
        
        return longest_pal_len + 1 if longest_pal_len != len(s) else longest_pal_len
