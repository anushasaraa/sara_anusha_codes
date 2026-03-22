class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        flag = 0
        hash = {}
        check = set()
        sub = s.split(" ")
        if len(sub) != len(pattern):
            return False
        i = 0
        for c in pattern:
            if c in hash:
                if hash[c] == sub[i]:
                    flag += 0
                else:
                    flag += 1
            elif sub[i] not in check:
                hash[c] = sub[i]
                check.add(sub[i])
            else:
                return False
            i += 1
        return True if flag == 0 else False
